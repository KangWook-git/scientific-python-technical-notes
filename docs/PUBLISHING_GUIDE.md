# Publishing this collection

## Recommended arrangement

Use GitHub for evolving source notebooks and a reading guide. Preserve a defined release in Zenodo when the files and metadata are ready. A direct Zenodo upload is also suitable if the main purpose is a stable personal and scholarly archive.

Suggested repository name: `scientific-python-technical-notes`

Suggested release tag: `v1.0.0`

Suggested release title: `Scientific Python Technical Notes — Revised English Edition 1.0.0`

## GitHub preparation

1. Review the notebooks and the execution report.
2. Select a license, add its files, and make README and CITATION.cff consistent with it.
3. Create or select the intended repository. Extract this package and place its contents at the repository root; do not merely upload the ZIP as the only readable repository item.
4. Commit notebooks, scripts, requirements, documentation, provenance, and citation metadata. Keep temporary environments and output directories excluded.
5. Check the README links and displayed notebooks on GitHub. HTML exports are downloadable documents; they do not become a hosted website merely because they are committed.
6. Add the actual repository URL to CITATION.cff.
7. If using Zenodo integration, connect and enable the repository before making the release.
8. Create the `v1.0.0` tag and release; attach the complete release ZIP if desired.

## Zenodo through GitHub

Enable the intended public repository in Zenodo's GitHub integration. A new GitHub release can then be archived as a linked Zenodo version. Check the processed record rather than assuming a commit has created an archive. The CITATION.cff supplies citation metadata; no `.zenodo.json` is included here to avoid an unnoticed competing metadata source.

After the DOI is assigned, add the actual version DOI and repository URL to citation and README information. That DOI was assigned after the release snapshot, so a follow-up commit updating the living README does not retroactively change the archived release. A concept DOI can represent the version family, while a version DOI identifies a particular archived set of files.

## Direct Zenodo upload

Create a new record for this English collection unless an existing record intentionally represents the same evolving work. Upload the complete ZIP and, if useful, the individual English notebooks and the README. Use the title, description, and keywords in ZENODO_METADATA.md. Select the license you have chosen and verify the actual uploaded file list before publishing.

For later substantial file revisions of the same collection, use New version in the existing record. Metadata corrections alone can be handled separately. Keep the notebook edition version, citation version, ZIP filename, and record Version field consistent.

## Suggested release description

This first revised English edition contains 15 scientific Python technical notes covering P0–P13, with short and expanded P5 reading routes. It connects mathematical meaning to numerical objects and verification evidence. Original executable examples and source provenance are retained with documented portability and numerical repairs. The release includes executed notebooks, HTML exports, a reproducible runner, tested dependencies, citation metadata, and a review and execution report. Illustrative wood and multiphysics laws are not presented as experimentally validated models.

## Official instructions

- [GitHub: citing content and Zenodo integration](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)
- [Zenodo: enable a repository](https://help.zenodo.org/docs/github/enable-repository/)
- [Zenodo: archive a GitHub release](https://help.zenodo.org/docs/github/archive-software/github-upload/)
- [Zenodo: citation metadata](https://help.zenodo.org/docs/github/describe-software/)
- [Zenodo: manage versions](https://help.zenodo.org/docs/deposit/manage-versions/)

This package is prepared for publication. It does not itself create a repository, assign a DOI, select a license, or publish a record.
