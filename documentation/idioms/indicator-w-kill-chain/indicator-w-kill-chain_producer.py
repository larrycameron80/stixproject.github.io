#!/usr/bin/env python

from stix.indicator import Indicator
from stix.core import STIXPackage
from stix.core.ttps import TTP

from stix.common.kill_chains import KillChain, KillChainPhase, KillChainPhaseReference


def main():
    stix_pkg = STIXPackage()

    # make indicator
    ind = Indicator()
    ind.title = "Malicious executable"
    ind.description = "Resident binary which implements infostealing and credit card grabber"

    # link to "Installation" phase and kill chain by ID values
    infect = KillChainPhase(name="Infect Machine")
    exfil = KillChainPhase(name="Exfiltrate Data")
    mychain = KillChain(name="Organization-specific Kill Chain")

    mychain.kill_chain_phases = [infect, exfil]
    stix_pkg.ttps.add_ttp(TTP())
    stix_pkg.ttps.kill_chains.append(mychain)
    stix_pkg.add_indicator(ind)

    # add referenced phase to indicator
    ind.kill_chain_phases.append(KillChainPhaseReference(phase_id=infect.phase_id, kill_chain_id=mychain.id_))

    print(stix_pkg.to_xml(encoding=None))

if __name__ == "__main__":
    main()
