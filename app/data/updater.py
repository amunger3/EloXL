from static import LeagueConfigs
from run_calcs import EloRunCalc
import pandas as pd

# NOTE: this file must be run from the project root to load the existing HDF Store

LC = LeagueConfigs()
hdf = pd.HDFStore('fbd_storage.h5')


def hdf5_handler(lg_key='PL'):

    lga_hdf = lg_key.lower()

    # Updating arrays
    if hdf.__contains__(lga_hdf):
        print("data present at {0}...deleting key".format(lga_hdf))
        hdf.remove(lga_hdf)

    pl_erc = EloRunCalc(LC._IDS[lg_key], season='2020', stage='REGULAR_SEASON', status='FINISHED')
    print("Storing DataFrame at /{0}".format(lga_hdf))
    df_comp = pl_erc.run_calcs()
    pd_comp = pd.DataFrame.from_dict(df_comp['data'], orient='index')
    pd_comp.to_hdf('fbd_storage.h5', lga_hdf)
    print("Storage of /{0} complete...".format(lga_hdf))
    hdf.close()

    return


if __name__ == '__main__':
    active_comps = ['BL', 'FL1', 'PL', 'ELC', 'PD', 'SA', 'PPL', 'DED']
    for comp in active_comps:
        print('Updating {0}'.format(comp))
        hdf5_handler(lg_key=comp)
