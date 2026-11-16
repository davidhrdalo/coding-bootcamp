# Thin wrapper for macOS and Linux. Everything lives in run.py so Windows can use it too:
#   Windows:  py run.py week0      Mac/Linux:  make week0   (same as python3 run.py week0)
PYTHON ?= python3
TASKS := setup setup-ts setup-web test week0 week1 week2 week3 week4 week5 week6 week7 web web-dom web-api web-react web-typecheck theory ts ts0 ts1 ts2 typecheck swift swift0 swift1 swift2 sql sql1 sql2 sql3 sql4 verify

.PHONY: $(TASKS)
$(TASKS):
	@$(PYTHON) run.py $@
