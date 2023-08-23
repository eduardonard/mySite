from flask import Blueprint, render_template

calculators = Blueprint("calculators", __name__)


@calculators.route("/finance")
def finance():
    return render_template("calculators/finance.html")

@calculators.route("/finance/loan")
def financeLoan():
    return render_template("calculators/finance/loan.html")

#####################################################INVESTING ROUTES#########################################
@calculators.route("/investing")
def investing():
    return render_template("calculators/investing.html")

@calculators.route("/investing/compoundInterest/DCA")
def investingCompoundInterestDCA():
    return render_template("calculators/investing/compoundInterestDCA.html")

@calculators.route("/investing/compoundInterest/LumpSum")
def investingCompoundInterestLumpSum():
    return render_template("calculators/investing/compoundInterestLumpSum.html")

@calculators.route("/investing/compoundInterest/PAC")
def investingCompoundInterestPAC():
    return render_template("calculators/investing/compoundInterestPAC.html")

#####################################################HEALTH ROUTES#########################################
@calculators.route("/health")
def health():
    return render_template("calculators/health.html")

@calculators.route("/health/BMI")
def healthBMI():
    return render_template("calculators/health/BMI.html")

#####################################################OTHER ROUTES#########################################
@calculators.route("/other")
def other():
    return render_template("calculators/otherhtml")