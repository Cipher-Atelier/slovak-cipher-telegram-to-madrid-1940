# Slovak cipher telegram to Madrid (11 November 1940)

A Slovak diplomatic telegram addressed to Madrid on 11 November 1940, catalogued as HCP125. It uses a letter-substitution cipher.

## Current result — 11 October 2026

This is a partial candidate substitution reading, with a qualified interpretation suggesting negotiations, a Bratislava proposal and an envoy. Positions 1–77 fitted the key; positions 78–97 were withheld. Five cipher letters have only one training occurrence, and `c`, `f`, `h`, `q` have none. Filled values for unused entries are not recovered historical mappings.

| Evidence layer | Open this |
| --- | --- |
| Original | [HCP125 catalogue](https://crypto.hcportal.eu/dashboard/cryptograms/125) · [source image](https://api.hcportal.eu/media/331/12921655394769.jpg) |
| Recorded signs / frozen candidate key | [Position ledger](verification/readings/evidence/Madrid1940_Forward_Evidence/mzv_c1940/pilot_v4/forward_diagnostic/FROZEN_POSITION_LEDGER.tsv) · [key](verification/readings/evidence/Madrid1940_Forward_Evidence/mzv_c1940/pilot_v4/forward_diagnostic/FROZEN_SELECTED_KEY.json) |
| First literal / later alternative | [First withheld output](verification/readings/evidence/Madrid1940_Forward_Evidence/mzv_c1940/pilot_v4/forward_diagnostic/HELDOUT_FIRST_EVALUATION.json) · [post-test source audit](verification/readings/evidence/Madrid1940_Forward_Evidence/mzv_c1940/pilot_v4/forward_diagnostic/HELDOUT_POST_SOURCE_AUDIT.json) |
| Qualified interpretation | [Research account](madrid-1940/README.md) |

The first withheld output is `vyslancatukrokovaoiu`. A later image-supported encrypted-source `n → m` change at position 95 gives `vyslancatukrokovaniu` under the unchanged key. Its interpretation, “the envoy here for negotiations”, is a post-test alternative. At position 69, source alternatives `u/n` produce decoded `d/o`; an editorial `n` would change the output. [Check `n/k/a → o/c/h` and the later correction](READING_GUIDE.md#check-one-example-by-hand).

**Unresolved / missing:** damaged wording, source ambiguities and weak mappings remain; no complete English translation is included. The 9 October residual audit accepted no new letters. The first result remains preserved separately from the later version, and the consumed holdout cannot become a fresh test.

## Research update — 9 October 2026

Read the [new check and its limits](research-updates/2026-10-09-residual-audit.md). This update is documentation; new experiment scripts are not included.

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
