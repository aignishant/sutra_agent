# `make` is not used in this project; ./m is the driver (plan §17.9, Day 0 §3.2).
# This shim exists only so that muscle memory and the plan's older `make check` still work.
check:
	@bash ./m check
