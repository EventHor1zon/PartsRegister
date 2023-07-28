from dataclasses import dataclass


@dataclass
class PartCode:
    typename: str
    shortname: str
    typecode: int


partcodes = [
    PartCode(typename="Adhesives and Chemical", shortname="adchem", typecode=14),
    PartCode(typename="Applications", shortname="apps", typecode=64),
    PartCode(typename="Assembly", shortname="asm", typecode=1),
    PartCode(typename="Battery", shortname="batt", typecode=16),
    PartCode(typename="Cadence Design Block", shortname="cad_db", typecode=34),
    PartCode(typename="Capacitor", shortname="cap", typecode=3),
    PartCode(typename="Configuration File", shortname="conf", typecode=46),
    PartCode(typename="Connector", shortname="conn", typecode=10),
    PartCode(
        typename="COTS Electromechanic Device", shortname="cots_emdev", typecode=30
    ),
    PartCode(typename="COTS Mechanical Part", shortname="cots_mecdev", typecode=31),
    PartCode(typename="Crystal or Oscillator", shortname="osc", typecode=44),
    PartCode(typename="Custom Mechanical Parts", shortname="cust_mech", typecode=20),
    PartCode(typename="Custom Product", shortname="cust_prod", typecode=36),
    PartCode(typename="Custom Service", shortname="cust_serv", typecode=37),
    PartCode(typename="Customer Mechanical Parts", shortname="cstm_mech", typecode=24),
    PartCode(typename="Design Only", shortname="desg", typecode=26),
    PartCode(typename="Diode", shortname="diode", typecode=6),
    PartCode(typename="Enclosure/Metal Parts", shortname="encl_part", typecode=12),
    PartCode(typename="Firmware/On-board Software", shortname="fw", typecode=18),
    PartCode(typename="Fixing", shortname="fixs", typecode=13),
    PartCode(typename="Fuse", shortname="fuse", typecode=38),
    PartCode(typename="IC Digital (retired)", shortname="ic_old", typecode=5),
    PartCode(typename="Integrated Circuit", shortname="ic", typecode=4),
    PartCode(typename="Misc Electric Part", shortname="elec_part", typecode=32),
    PartCode(typename="MOSFET", shortname="mosfet", typecode=8),
    PartCode(typename="Motor", shortname="motor", typecode=29),
    PartCode(typename="PCB", shortname="pcb", typecode=11),
    PartCode(typename="Populated PCB Assembly", shortname="popl_pcb", typecode=25),
    PartCode(typename="Product Range", shortname="prod_rng", typecode=0),
    PartCode(typename="Relay", shortname="relay", typecode=23),
    PartCode(typename="Reseller Product", shortname="resell", typecode=35),
    PartCode(typename="Resistor", shortname="res", typecode=2),
    PartCode(typename="Shipping Material", shortname="ship_mat", typecode=17),
    PartCode(typename="Solar Cell", shortname="sol_cell", typecode=15),
    PartCode(typename="Switch", shortname="switch", typecode=41),
    PartCode(typename="Test Equipment", shortname="test", typecode=50),
    PartCode(typename="Test Jig/Test Box", shortname="test_box", typecode=22),
    PartCode(typename="Test Point", shortname="test_pt", typecode=43),
    PartCode(typename="Test Software", shortname="test_sw", typecode=19),
    PartCode(typename="Thermal", shortname="thermal", typecode=33),
    PartCode(typename="Thermistor", shortname="thermist", typecode=39),
    PartCode(typename="Tooling", shortname="tooling", typecode=28),
    PartCode(typename="Transformer", shortname="transfmr", typecode=42),
    PartCode(typename="Transistor", shortname="transist", typecode=7),
    PartCode(typename="Varistor", shortname="varist", typecode=40),
    PartCode(typename="Wire/Harness/Interconnect", shortname="harness", typecode=27),
    PartCode(typename="Zener Diode", shortname="zener", typecode=45),
    PartCode(typename="Lab Equipment", shortname="lab", typecode=60),
    PartCode(typename="MRP Line Item", shortname="mrp_item", typecode=47),
]
