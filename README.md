# Deskera Pagerank
Pagerank PoC for Deskera

## File and folder descriptions
The file and folder name descriptions are as follows:
- `./dist/` is the directory that contains the binary and its resources compiled from the Python code. `gtpageranktest_txt` inside it is the actual binary
- `convert.py` is a small script written using the `networkx` library that converts the `.edgelist` format to `.graphml` format.
- `facebook.graphml` is a graph file corresponding to an undirected unweighted graph downloaded from the internet.
- `gt-pagerank-test.py` is a Python script used for testing the `graph-tool` library and it's applications.
- `gtpageranktest.py` is the same as `gt-pagerank-test.py` with the only difference being the use of a `parser` for inputting the `.graphml` file directly from command line.
- `gtpageranktest_txt.py` is a Python script for the final PoC and contains functionality for converting the `.edgelist` format to a `graph-tool` Graph object.
- `ig-pagerank-test.py` is a Python script used for testing the `igraph` library and it's applications.
- `nk-pagerank-test.py` is a Python script used for testing the `networkit` library and it's applications.
- `nx-pagerank-test.py` is a Python script used for testing the `networkx` library and it's applications.
- `populate.py` is Python script used for generating `testgraph_big.edgelist` for testing the binary on big graphs.
- `test_manual.rs` is a Rust script used for testing the `gtpageranktest_txt` binary in Rust. I allows manually setting the location of the binary as well as the `.edgelist` file.
- `test.rs` is a Rust script for testing the final binary and uses functional approach for better integration into production.
- `usewithgt.py` is a Python script for converting the `.edgelist` format to a `graph-tool` Graph object. It has not been incorporated in `gtpageranktest_txt.py`.

## The `.edgelist` format
The salient features of the `.edgelist` format are:
- Lines starting with `#` (treated as comments) and empty lines are ignored.
- Every line in the file corresponds to a node between `node 1` `n1` and `node 2` `n2` for the first 2 `integer` values with the third `float` value corresponding to the weight `w` of the particular edge.
- More types of weights can later be incorporated in the format with appropriate changes to the algorithm in `usewithgt.py`.
