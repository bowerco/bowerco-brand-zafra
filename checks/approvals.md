# Approvals

## Who approves what (TODO: names and turnaround from the brand)
| Content | Approver | Turnaround |
|---|---|---|
| Stories | TODO | TODO |
| Feed posts, carousels, reels, TikToks | TODO | TODO |
| Anything with a price, claim or retailer name | TODO | TODO |
| Ramadan and Eid campaign | TODO | TODO |

## Flow
1. Bower drafts in `content/drafts/` (media in `content/drafts/media/<piece>/`), runs `./check` and `checks/rules.md`.
2. **Fonts:** while only the Euclid Flex trial is in the repo, nothing with headline type is sent to Zafra (trial licence). Send pieces without type, or wait for the licensed files.
3. Only drafts with no FAIL go to review. BLOCKED items go with the open question attached.
4. Reviewer replies: **OK**, **OK with edits** (edits written inline), or **Change request**.
5. Change request: Bower edits, re-runs checks, bumps `version`, resends.
6. On OK: move to `content/approved/`, set `status: approved`, `approved_by`, `approved_on`.
7. After posting: `status: published`, add the post URL, log results in `results/instagram.csv` or `results/tiktok.csv`.

## Change request format
`[piece id] · [frame/line] · [what to change] · [why, optional]`
