# Read this investigation

[Repository overview](README.md) · [Technical verification](verification/README.md)

## Understand the document

A Slovak diplomatic telegram addressed to Madrid on 11 November 1940, catalogued as HCP125. It uses a letter-substitution cipher.

Start with the [source catalogue or manuscript](https://crypto.hcportal.eu/dashboard/cryptograms/125). It identifies the historical object. The source image is the evidence; the tables in this repository are recorded readings of that evidence.

## Read the current result

The candidate reading suggests negotiations, Bratislava, a proposal and an envoy. It remains partial: several words are damaged, some key values have very little evidence, and a later source correction must be distinguished from the first test.

Open [First withheld-span result](verification/readings/evidence/Madrid1940_Forward_Evidence/mzv_c1940/pilot_v4/forward_diagnostic/HELDOUT_FIRST_EVALUATION.json) and the [research account](madrid-1940/README.md). A literal preserves the recorded output before making it smoother to read. An English explanation or translation adds interpretation and should not silently repair it.

Example:

```text
vyslancatukrokovaoiu
```

This is the first saved output for the withheld span. A later image-supported alternative changes it to vyslancatukrokovaniu; that later version is not the original test result.

There is no complete fluent plaintext or exact original 20/20 recovery. Adding spaces is different from changing letters: do not turn damaged words into established treaty terminology without evidence.

## Check one example by hand

1. Open the [position ledger](verification/readings/evidence/Madrid1940_Forward_Evidence/mzv_c1940/pilot_v4/forward_diagnostic/FROZEN_POSITION_LEDGER.tsv). Its columns distinguish the frozen source letter/output from the source-v2 snapshot. That snapshot does not include the subsequent heldout source audit; its position 95 still records `n`. The later preference is saved separately in step 3.
2. The first three rows record:

| Position | Frozen cipher letter | Frozen output |
| --- | --- | --- |
| 1 | `n` | `o` |
| 2 | `k` | `c` |
| 3 | `a` | `h` |

These give `och`, the start of the training output in the [frozen-key record](verification/readings/evidence/Madrid1940_Forward_Evidence/mzv_c1940/pilot_v4/forward_diagnostic/FROZEN_SELECTED_KEY.json). The key string lists output letters in cipher-alphabet order `a` through `z`; it is a substitution table, not a word to paste onto the message.
3. Compare position 95 with the [later source audit](verification/readings/evidence/Madrid1940_Forward_Evidence/mzv_c1940/pilot_v4/forward_diagnostic/HELDOUT_POST_SOURCE_AUDIT.json): the initial reading used `n → o`; the later preference uses `m → n`, with the same key. This explains the two different heldout strings.
4. Compare the disputed sign yourself in the [original image](https://api.hcportal.eu/media/331/12921655394769.jpg). Source alternatives remain documented; the later preference is not an exact first-test recovery.

Positions 1–77 were used for fitting; 78–97 were withheld. Some key entries occur only once in training, and `c`, `f`, `h`, `q` had no training examples. Filled values for those absent letters are not recovered historical mappings.

## Choose the check you want

- **Understand the result:** read the literal/test result beside the research account. You can do this in GitHub without installing anything.
- **Check the calculation:** follow the example above, then [run the supported Python check](verification/README.md). This verifies the saved transformation or declared model.
- **Check the source:** compare recorded signs with the original image and retain disagreements. Scans/crops are not included; obtain access under the provider’s terms. Original coordinates, when present, refer to the specified image version.
- **Evaluate the historical reading:** examine alternative signs, key evidence, language, document boundaries and prior readings. A successful calculation does not settle these questions.

To report a problem, use [Work on existing research](https://github.com/Cipher-Atelier/slovak-cipher-telegram-to-madrid-1940/issues/new?template=research.yml). Give the file, row/position, source reference, your observation, and what changes in the output. Distinguish a different source reading from a changed key or an editorial interpretation.

## What the files mean

| Open this | It contains |
| --- | --- |
| [Research account](madrid-1940/README.md) | Historical context, method, interpretation, credits and limits |
| [First withheld-span result](verification/readings/evidence/Madrid1940_Forward_Evidence/mzv_c1940/pilot_v4/forward_diagnostic/HELDOUT_FIRST_EVALUATION.json) | The saved text or bounded test result |
| [Position-by-position letter ledger](verification/readings/evidence/Madrid1940_Forward_Evidence/mzv_c1940/pilot_v4/forward_diagnostic/FROZEN_POSITION_LEDGER.tsv) | The recorded input/assignments used in the example |
| [Frozen candidate key](verification/readings/evidence/Madrid1940_Forward_Evidence/mzv_c1940/pilot_v4/forward_diagnostic/FROZEN_SELECTED_KEY.json) | The proposed transformation, historical key, or tested assumptions |
| [Technical verification](verification/README.md) | Setup, command, expected output and what the check covers |
| [Source scope](verification/TOPIC_SCOPE_INDEX.json) | Machine-readable release boundaries and omitted material |
| [Publication provenance](SOURCE_PROVENANCE.json) | Where this package came from and what documentation changed |

CSV and TSV are tables: GitHub or a spreadsheet can display them. TSV uses tabs between columns. JSON stores named fields and lists; `null` means no value in that field, and its interpretation depends on the record. You do not need to start by reading every JSON file.

## Terms used in the research

- **Ciphertext:** the recorded encrypted signs or letters.
- **Key/mapping:** the rule assigning output to a cipher sign. It may be a hypothesis, a surviving historical key, or an assumption in a test; those are different kinds of evidence.
- **Literal reading:** the saved output with gaps and awkward wording retained, before editorial translation or repair.
- **Coverage:** how many recorded positions receive a value. It does not measure how many values are historically correct.
- **Frozen:** saved unchanged at a particular stage so a later correction cannot replace an earlier test result.
- **Replay:** applying saved rules to saved inputs again. It checks reproducibility within the declared scope.
- **Training/heldout:** material used to fit a rule, and material excluded from that fitting. Prior viewing or later correction can limit how independent a heldout test is; read the case-specific account.
