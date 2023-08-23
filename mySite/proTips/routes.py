from flask import Blueprint, render_template

proTips = Blueprint("proTips", __name__)


@proTips.route("/finance")
def finance():
    return render_template("proTips/finance.html")

@proTips.route("/finance/loan")
def financeLoan():
    return render_template("proTips/finance/loan.html")

#####################################################INVESTING ROUTES#########################################
@proTips.route("/investing")
def investing():
    return render_template("proTips/investing.html")

@proTips.route("/investing/compoundInterest/DCA")
def investingCompoundInterestDCA():
    return render_template("proTips/investing/compoundInterestDCA.html")

@proTips.route("/investing/compoundInterest/LumpSum")
def investingCompoundInterestLumpSum():
    return render_template("proTips/investing/compoundInterestLumpSum.html")

@proTips.route("/investing/compoundInterest/PAC")
def investingCompoundInterestPAC():
    return render_template("proTips/investing/compoundInterestPAC.html")

#####################################################HEALTH ROUTES#########################################
@proTips.route("/health")
def health():
    return render_template("proTips/health.html")

@proTips.route("/health/BMI")
def healthBMI():
    return render_template("proTips/health/BMI.html")

#####################################################OTHER ROUTES#########################################
@proTips.route("/other")
def other():
    return render_template("proTips/otherhtml")