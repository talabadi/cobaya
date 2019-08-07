from cobaya.likelihoods._planck_clik_prototype import _planck_clik_prototype
from cobaya.likelihoods._planck_clik_prototype import install as install_common
from cobaya.likelihoods._planck_clik_prototype import is_installed as is_installed_common


class planck_2018_plikHM_TTTEEE_lite(_planck_clik_prototype):
    defaults = """
        # Planck 2015 release: high-ell, CMB temperature only likelihood
        # See https://wiki.cosmos.esa.int/planckpla2015/index.php/CMB_spectrum_%26_Likelihood_Code

        likelihood:
          planck_2018_plikHM_TTTEEE_lite:
            path:
            clik_file: baseline/plc_3.0/hi_l/plik_lite/plik_lite_v22_TTTEEE.clik
            product_id: "1900"
            # Aliases for automatic covariance matrix
            renames: [plikHM_TTTEEE]
            # Speed in evaluations/second
            speed: 500
            # Nuisance parameters (do not change)
            nuisance: [calib]"""


def is_installed(**kwargs):
    kwargs["name"] = __name__.split(".")[-1]
    return is_installed_common(**kwargs)


def install(**kwargs):
    kwargs["name"] = __name__.split(".")[-1]
    return install_common(**kwargs)
