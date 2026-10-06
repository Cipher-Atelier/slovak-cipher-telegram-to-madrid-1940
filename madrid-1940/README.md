# Madrid 1940: a strong partial reading of HCP125

Research status as of 5 October 2026: **strong partial reading; unresolved source signs, single-occurrence mappings and anomalous wording remain.**

## Research task

Test the substitution cipher in MZV message 12009/1940, dated 11 November 1940 and addressed **to Madrid**. HCPortal identifies the sender as Országh, the recipient as the Slovak legation in Madrid, and the source as the Slovak National Archive, fond MZV, box 39. The original title is *Odpoveď na 775*. Madrid is the destination, not an established place of composition. [Catalogue](https://crypto.hcportal.eu/dashboard/cryptograms/125), [source image](https://api.hcportal.eu/media/331/12921655394769.jpg).

## Tests completed

The 97-position working transcription was split into 77 training positions and 20 withheld positions. Earlier reverse-oriented pilots were not coherent. A period-Slovak model subsequently passed a separately frozen synthetic recovery check, with 379/380 scored training letters and 100/100 heldout letters recovered. Those are synthetic-control results, not measurements of manuscript accuracy.

A predeclared forward-orientation diagnostic produced sustained Slovak material. Five known-key checks verified the orientation mechanics; they were not five new blind recovery experiments. The selected key was frozen before its first application to the withheld 20 positions. All 20 used mappings already observed in training.

The first frozen-key heldout output was exactly:

`vyslancatukrokovaoiu`

A later source-only image inspection preferred ciphertext m rather than n at position 95. Applying the unchanged key to that preferred reading gives:

`vyslancatukrokovaniu`

The latter can be segmented as *vyslanca tu k rokovaniu*, “the envoy here for negotiations.” It is a **post-test, image-supported alternative**, not an initial exact 20/20 recovery. Source alternatives remain at positions 78, 83 and 95. The historical holdout has been consumed and cannot be reused as a fresh test.

## Result and interpretation

The frozen training output, without silent repairs, is:

`ochotnyso?rokovatoobcmojusmluvuzbratislavegnechposlunavrhapoperiaspadielskeho`

It suggests negotiations concerning a treaty, Bratislava, a proposal and authorization of a Spanish envoy. A fluent translation would require corrections beyond adding spaces or accents. In particular, `obcmoju` is unresolved and must not be printed as an established trade-related adjective; `zbratislave`, the separate `g`, `poperia` and `spadielskeho` retain difficulties. The case ending in `smluvu` also prevents an unqualified grammatical reconstruction.

The candidate alphabet is incomplete. Cipher c, f, h and q were absent from training, so their filled-in values are arbitrary. Five mappings, j, t, u, v and z, each occur only once in training. Repeated mappings and coherent phrases are useful evidence, but neither supplies a historical plaintext against which every character can be scored.

## Unresolved questions

- Which retained glyph alternatives are correct, especially in the short heldout span?
- Are the remaining anomalies transcription errors, enciphering errors, or incorrect candidate mappings?
- Can another independently identified same-key text confirm the singletons and missing alphabet entries?
- Does a historical cleartext or earlier document-specific reading survive?

No complete plaintext, unique full alphabet or first-decipherment priority is claimed.

## Public sources and earlier-work credit

- [HCPortal HCP125](https://crypto.hcportal.eu/dashboard/cryptograms/125) and the [original digitized telegram](https://api.hcportal.eu/media/331/12921655394769.jpg), from the Slovak National Archive. HCPortal still labelled the record “Not solved” when its public metadata was checked on 5 October 2026; that is a catalogue field, not proof of novelty.
- Eugen Antal, Pavol Zajac and Otokar Grošek, [“Diplomatic Ciphers Used by Slovak Attaché During the WW2”](https://ep.liu.se/ecp/171/004/ecp2020_171_004.pdf), HistoCrypt 2020, pp. 21–30. This is prior scholarship on the cipher systems, not a published plaintext of this particular telegram located by the present check.

The public links identify the source and earlier scholarship. The numerical tests above report this investigation's experiments; the cited institutions have not certified the proposed reading.
