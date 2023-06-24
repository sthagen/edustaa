# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/edustaa/blob/default/sbom/cdx.json) with SHA256 checksum ([8cd1faf9 ...](https://git.sr.ht/~sthagen/edustaa/blob/default/sbom/cdx.json.sha256 "sha256:8cd1faf990a2118c0e3259a67a903b3b494b1a2c64af96a9e6de9ac5d2bd443d")).
<!--[[[end]]] (checksum: 49ce8b600a513eb7c33b6e2b6f789861)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                        | Version                                            | License     | Author          | Description (from packaging data)                                                                        |
|:--------------------------------------------|:---------------------------------------------------|:------------|:----------------|:---------------------------------------------------------------------------------------------------------|
| [msgspec](https://jcristharif.com/msgspec/) | [0.16.0](https://pypi.org/project/msgspec/0.16.0/) | BSD License | Jim Crist-Harif | A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML. |
<!--[[[end]]] (checksum: 2dace89c8af260977a52ea681ae1ed6f)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                 | Version                                                | License                              | Author         | Description (from packaging data)                 |
|:-----------------------------------------------------|:-------------------------------------------------------|:-------------------------------------|:---------------|:--------------------------------------------------|
| [certifi](https://github.com/certifi/python-certifi) | [2023.5.7](https://pypi.org/project/certifi/2023.5.7/) | Mozilla Public License 2.0 (MPL 2.0) | Kenneth Reitz  | Python package for providing Mozilla's CA Bundle. |
| [click](https://palletsprojects.com/p/click/)        | [8.1.3](https://pypi.org/project/click/8.1.3/)         | BSD License                          | Armin Ronacher | Composable command line interface toolkit         |
<!--[[[end]]] (checksum: f9ac0bb9466fdf070ccfee9554b8d751)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
msgspec==0.16.0
````
<!--[[[end]]] (checksum: 65c530d389ea3bf9a288fd12fdb4b161)-->
