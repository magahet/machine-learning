import pyweka


def reparse(results_file):
    t = pyweka.TestSuite(results_file=results_file)
    results = [t.parse_tree_output(r['raw_output']) for r in t.results]
    print results
    for i in range(len(t.results)):
        t.results[i]['results'] = results[i]
    t.save_results(results_file)
