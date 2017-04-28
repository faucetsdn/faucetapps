:version: 1.0.0
:copyright: 2015--2017 The Contributors

.. meta::
  :keywords: OpenFlow, Ryu, Faucet, VLAN, SDN, CouchDB, CouchApp

===================
Faucet Applications
===================

Faucet allows apps that can be written to CouchDB (flows) and InfluxDB (stats).  The information in these databases are near real-time data from actual switches collected by Gauge controller.  Flows are collected every 60 seconds and stats are collected every 10 seconds.
          .
List of Applications:

   1. `Flowinfo <faucetapps/flowinfo/>`_ - provides flows on different switches across various tables.



