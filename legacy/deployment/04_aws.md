# 04 · Amazon Web Services — free-tier deployment options

> ⚠️ **This file could not be verified against a live AWS pricing page this session** —
> `aws.amazon.com/free/` and `aws.amazon.com/free/free-tier-faqs/` both failed to return
> extractable content when fetched on 2026-08-21 (likely heavy client-side rendering on those
> pages). Every figure below is a long-stable, widely and consistently documented AWS fact
> (these specific numbers have been unchanged for years), **not a live-verified one** — per this
> project's own Principle 7/8, treat them as "look this up before you pin it," not as fact.
> **Before running anything in this file, confirm current numbers at
> [aws.amazon.com/free](https://aws.amazon.com/free/)** and its linked FAQ.

---

## 1 · AWS's three free-tier categories

| Category | What it means | Expires? |
| --- | --- | --- |
| **Always Free** | A quota with no end date | Never |
| **12 Months Free** | An elevated quota, from account-creation date | Yes — 12 months, new accounts only |
| **Trials** | A short-term credit or elevated limit on a specific service | Yes — short, service-specific |

**⚠️ Recalled (verify before relying on these exact numbers):**

| Service | Category | Commonly documented grant |
| --- | --- | --- |
| **AWS Lambda** | Always Free | 1,000,000 requests/month **+** 400,000 GB-seconds of compute time/month, forever |
| **DynamoDB** | Always Free | 25 GB storage + 25 provisioned read/write capacity units |
| **AWS SSM Parameter Store** (standard parameters) | Always Free | free — the notably cheaper alternative to Secrets Manager, see [00_stay_free_safety.md](00_stay_free_safety.md) §5 |
| **EC2** | 12 Months Free | 750 hours/month of `t2.micro` (or `t3.micro` in regions where `t2.micro` isn't offered) |
| **S3** | 12 Months Free | 5 GB Standard storage |
| **RDS** | 12 Months Free | 750 hours/month of `db.t2/t3/t4g.micro` |
| **EKS control plane** | **Not free, any tier** | **$0.10/hour (~$73/month)** — flat fee, independent of usage; see §3 |
| **Fargate / App Runner** | **No free tier** | billed per vCPU-second/GB-second (Fargate) or per compute-second + request (App Runner) from the first second |

## 2 · Before you create anything

1. Read [00_stay_free_safety.md](00_stay_free_safety.md) §3 — AWS Budgets ships an actual
   one-click **"Zero spend budget"** template in the console, the closest any of the three
   major clouds gets to a genuine tripwire. Set it before anything else in this file.
2. **Never use the AWS root account for day-to-day work.** Create an IAM user (or, better, use
   IAM Identity Center) with only the permissions this file's commands need, and use that for
   everything below. This is standard AWS security guidance independent of the zero-budget
   angle — the root account should be used only for account-level tasks.

```powershell
winget install -e --id Amazon.AWSCLI
aws configure                 # access key, secret key, region, output format — for the IAM user, not root
aws sts get-caller-identity   # confirms which identity you're actually using
```

## 3 · Kubernetes on AWS: why EKS is the one to skip here

Unlike GCP's GKE and Azure's AKS, **Amazon EKS charges $0.10/hour for the control plane itself**
— roughly $73/month, with no free-tier waiver, whether or not you run a single pod. This is the
one place the three major clouds genuinely diverge, and it's the reason this folder's decision
table ([README.md](README.md) §2) points at `kind`/`k3d`
([01_local_docker_and_kubernetes.md](01_local_docker_and_kubernetes.md)) instead of EKS for
learning Kubernetes "the AWS way." If you specifically need to demonstrate EKS knowledge:
read AWS's own EKS documentation and write a parked walkthrough using the same discipline as
[day_087.md](../days/day_087.md) (first line says it was never run, dated sources, a
re-verification command) rather than actually running a cluster that bills by the hour whether
you use it or not.

## 4 · AWS Lambda — container-image deployment, inside the Always-Free grant

Lambda supports deploying a container image (up to 10 GB) instead of a zip — the natural fit for
an agent packaged the same way as [day_086.md](../days/day_086.md)'s Dockerfile:

```powershell
aws ecr create-repository --repository-name myagent
$loginPwd = aws ecr get-login-password --region us-east-1
$loginPwd | docker login --username AWS --password-stdin "$($env:AWS_ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com"

docker build -t myagent .
docker tag myagent:latest "$($env:AWS_ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com/myagent:latest"
docker push "$($env:AWS_ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com/myagent:latest"

aws lambda create-function `
  --function-name myagent `
  --package-type Image `
  --code "ImageUri=$($env:AWS_ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com/myagent:latest" `
  --role "arn:aws:iam::$($env:AWS_ACCOUNT_ID):role/lambda-basic-execution" `
  --memory-size 512 `
  --timeout 30 `
  --environment "Variables={GOOGLE_GENAI_USE_VERTEXAI=FALSE}"

aws lambda create-function-url-config --function-name myagent --auth-type NONE
```

| Command / flag | What it does |
| --- | --- |
| `ecr create-repository` | ECR is AWS's container registry; Lambda pulls the image from here, not from Docker Hub |
| `--package-type Image` | tells Lambda this is a container-image function, not a zip-based one |
| `--role arn:...lambda-basic-execution` | the IAM role Lambda assumes at runtime — must exist first (`aws iam create-role` + attach the `AWSLambdaBasicExecutionRole` policy) |
| `--memory-size 512` | Lambda's GB-second billing (and the free-tier count) is `memory × duration` — smaller memory means more free invocations before the 400,000 GB-second allowance is used |
| `create-function-url-config --auth-type NONE` | gives the function a public HTTPS URL directly, no API Gateway needed — the simplest way to get a reachable endpoint for a demo |

⚠️ A Lambda function is not "always on" — each request either reuses a warm container or pays a
cold-start penalty. For an agent that calls an LLM (already seconds of latency), this is usually
an acceptable trade for staying inside the Always-Free grant.

## 5 · EC2 — the 12-months-free VM (with a literal clock)

```powershell
aws ec2 run-instances `
  --image-id ami-0abcdef1234567890 `
  --instance-type t3.micro `
  --key-name my-key `
  --security-group-ids sg-0123456789abcdef0 `
  --count 1
```

| Flag | What it does |
| --- | --- |
| `--instance-type t3.micro` | the type the 12-months-free grant covers (or `t2.micro` — region-dependent, ⚠️ confirm at signup) |
| `--security-group-ids` | AWS security groups default to **deny all inbound** — you must explicitly allow the port your agent listens on, same idea as GCP's firewall rule in [02_gcp.md](02_gcp.md) §5 |

**Calendar the 12-month expiry the day you launch this.** Unlike Lambda's Always-Free grant,
EC2's free hours stop being free on a fixed date from account creation, not from this
instance's launch date — an easy distinction to lose track of months later.

## 6 · Terraform for AWS

```hcl
# main.tf
terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

provider "aws" { region = "us-east-1" }

resource "aws_lambda_function" "myagent" {
  function_name = "myagent"
  package_type  = "Image"
  image_uri     = "${var.account_id}.dkr.ecr.us-east-1.amazonaws.com/myagent:latest"
  role          = aws_iam_role.lambda_exec.arn
  memory_size   = 512
  timeout       = 30

  environment {
    variables = { GOOGLE_GENAI_USE_VERTEXAI = "FALSE" }
  }
}

resource "aws_iam_role" "lambda_exec" {
  name = "myagent-lambda-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "basic_exec" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function_url" "myagent_url" {
  function_name      = aws_lambda_function.myagent.function_name
  authorization_type = "NONE"
}
```

| Block | What it does |
| --- | --- |
| `aws_lambda_function` | the declarative equivalent of §4's `aws lambda create-function` |
| `aws_iam_role` + `assume_role_policy` | the trust policy saying "the Lambda service may assume this role" — required before Lambda can run as anything |
| `aws_iam_role_policy_attachment` | attaches AWS's own managed basic-execution policy (CloudWatch Logs write access) rather than hand-writing an equivalent — least-effort least-privilege |
| `aws_lambda_function_url` | the declarative equivalent of `create-function-url-config` |

```powershell
terraform init
terraform plan     # review before applying — see 05_terraform.md §4
terraform apply
terraform destroy  # the moment you're done testing
```

## 7 · Cleanup

```powershell
aws lambda delete-function --function-name myagent
aws ecr delete-repository --repository-name myagent --force
aws ec2 terminate-instances --instance-ids i-0123456789abcdef0    # terminate, not just stop
```

⚠️ **`stop-instances` is not enough.** A stopped EC2 instance no longer bills for compute, but
its attached EBS volume keeps billing (small, but real, and easy to forget for months). Use
`terminate-instances` when you're actually done, and separately check
`aws ec2 describe-volumes` for anything left over.
