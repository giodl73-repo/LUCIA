# What these native checks establish

LUCIA's product-local Rust layer checks supplied people-history fields and
compares declared event/person/story-path requirements. It does not replace the
established story or interpret source documents. Reference paths and anchors are
inert supplied strings: the app never fetches, opens or verifies them.

History-only validation does not parse/use the profile. Comparison invokes the
same native validator plus profile comparison. Native output remains exact:
pass can coexist with warning findings or empty records/requirements; duplicate
IDs and an event's agreement with its enclosing era are not certified; required
paths compare as strings. Framing detection is case-insensitive substring search
over framing_notes only. Empty forbidden patterns match all supplied notes.
Consequence text is an input claim, not a demonstrated causal mechanism.

Unknown fields follow native Serde behavior and are reported as ignored field
paths in Serde notation, not JSON Pointer. Recognized duplicate fields retain
native parse errors. The typed projection may materialize defaults and omit
extensions. It is not replacement source: exact original/current/request exports
retain supplied inputs. LF-copy actions explicitly remove a leading BOM and
convert line endings while keeping opened original bytes separately.

Browser admission is separate from native semantics: 2 MiB request, 256 KiB
history, 128 KiB compared profile, 2 MiB report; 32 eras, 256 persons, 512 events,
2,048 references, 4,096 actor/place entries, 128 framing notes, 1,024 ignored
fields per input and 4,096 UTF-8 bytes per interpreted string. Profile required
lists are each limited to 512 entries and framing patterns to 128. Original
native CLI limits remain separate. Worker deadlines and a 64 MiB memory ceiling
bound this browser task.

The synthetic examples assert no real cultural/historical facts. Chapters,
manuscript architecture, rubric evolution, selected specialist/board review,
the Achebe Test and downstream consumer-contract authority retain their own
owners. No historical truth, source verification, factual/causal endorsement,
chapter lock, manuscript readiness or generic history library is claimed.
