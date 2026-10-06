# Slovak cipher telegram to Madrid (11 November 1940)

A Slovak diplomatic telegram addressed to Madrid on 11 November 1940, catalogued as HCP125. It uses a letter-substitution cipher.

## What has been found?

The candidate reading suggests negotiations, Bratislava, a proposal and an envoy. It remains partial: several words are damaged, some key values have very little evidence, and a later source correction must be distinguished from the first test.

A small example from the recorded result:

```text
vyslancatukrokovaoiu
```

This is the first saved output for the withheld span. A later image-supported alternative changes it to vyslancatukrokovaniu; that later version is not the original test result.

## Start reading

1. [Read the plain-language guide](READING_GUIDE.md): the document, result, file meanings and one worked check. No programming is required.
2. Open [First withheld-span result](verification/readings/evidence/Madrid1940_Forward_Evidence/mzv_c1940/pilot_v4/forward_diagnostic/HELDOUT_FIRST_EVALUATION.json) to inspect the saved text or test result itself.
3. Read the [research account](madrid-1940/README.md) for historical context, methods, earlier work and unresolved questions.

## How can I check it?

Follow the worked example in [the reading guide](READING_GUIDE.md#check-one-example-by-hand). It connects a source record, a key or model assumption, and the saved output. For an independent source check, use the [original-source entry](https://crypto.hcportal.eu/dashboard/cryptograms/125); images are linked, not redistributed here.

If you use Python, follow the [complete verification instructions](verification/README.md), including download/setup, expected results and troubleshooting. The command from this repository’s top-level folder is:

```sh
python3 verification/check_all.py
```

A successful run means the published files and declared calculation reproduce. It does not establish that every source sign or historical interpretation is correct.

## Precise research scope

Weaker partial forward-substitution reading, with damaged training output and singleton mappings. Preserve the first consumed test separately from post-test source correction; no exact 20/20 claim.

This is part of [Cipher-Atelier](https://github.com/Cipher-Atelier), founded by [Maxim Egorov](https://github.com/cayde-6). Explore the [research index](https://github.com/Cipher-Atelier/research-index), [contribution guide](https://github.com/Cipher-Atelier/.github/blob/main/CONTRIBUTING.md), and [step-by-step research workflow](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md).

Source credit and item-specific restrictions remain in the research records. Scans, crops, restricted materials and private correspondence are excluded. No new blanket licence is asserted. AI-assisted work requires evidence checking and does not constitute external human expert review.

[Publication provenance](SOURCE_PROVENANCE.json) records the source commit, retained file hashes and deliberate code/navigation adaptations. The original repository history remains intact.

## Contribute to this investigation

Read the current result and source limitations, then coordinate a bounded task in an existing issue or use [Work on existing research](https://github.com/Cipher-Atelier/slovak-cipher-telegram-to-madrid-1940/issues/new?template=research.yml). Fork the repository and submit a focused pull request with your evidence and checks. Independent replication and constructive alternative readings are welcome. See [Start here](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md) for the shared workflow.
