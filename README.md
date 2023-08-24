# suppression-test-python-mix

This repository is used to test our analysis code for studying suppressed warnings.
The focus here is on
 * Python repositories
 * the Pylint and Mypy
 * the histories of individual suppressions
 * mainly focus on **normal delete** + **Use multiple tools at the same time**

## Expected output of our analysis scripts

*TODO: Turn this into an automatically testable format, e.g., an expected JSON file*

* Suppression "# pylint: disable=unused-variable"
  * Introduced in commit 464f7c8da555169c4d0a835c26deacbc7d2f2ee3
  * Code on the same line changed (but suppression is not changed) in commit b90bb6cd43cace149990f3757cad014f2ef68dff
  * Removed in commit 151276c9e82f166777ae7f4c20d94f4e28a19cdb

* Suppression "# pylint: disable=unused-argument"
  * Introduced in commit ad4460acd3bbae6b1274ff017466406be00711e4
  * Became a useless suppression in commit 6ce1caeda40642dacc032043df45083233604885
  * Removed in commit 8e15b861e33082d7452b579bf734536f44add3f1

* Suppression "# type: ignore"
  * Introduced in b62b7a1ab990279067c6f3bea702509fec6eb1dc
  * Code on the same line changed (but suppression is not changed) in commit 8e15b861e33082d7452b579bf734536f44add3f1
  * (Never removed)
