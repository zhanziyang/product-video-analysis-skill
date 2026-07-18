# Product Video Analysis Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and verify a public-ready Agent Skill repository for complete product-video breakdowns.

**Architecture:** Keep activation instructions compact in `SKILL.md`; move heavy standards into references, reusable contracts into templates, and mechanical evidence collection into standard-library Python scripts. Use a JSON manifest validator and generated-media tests to prevent module regression and unverifiable completeness claims.

**Tech Stack:** Agent Skills Markdown/YAML, Python 3.10+ standard library, FFmpeg/FFprobe, unittest, GitHub Actions.

## Global Constraints

- Repository name: `product-video-analysis-skill`.
- Skill name: `product-video-analysis`.
- Public repository, maintained by owner, MIT License.
- General Agent Skills compatibility with Codex enhancement.
- New analysis detail never replaces any of the 25 required modules.
- Reverse-engineered parameters and intent are labeled Estimated or Inferred.

---

### Task 1: Skill contract and baseline regression

**Files:**
- Create: `skills/product-video-analysis/SKILL.md`
- Create: `tests/scenarios/01-module-regression.md`
- Create: `tests/expected/01-module-regression.md`
- Test: `tests/test_skill_structure.py`

**Interfaces:**
- Produces: valid skill frontmatter and references to the full analysis contract.

- [x] Write a failing structural test requiring valid frontmatter, compact trigger description, and all required reference links.
- [x] Record the observed baseline failure: animation detail was added while earlier modules were silently removed.
- [x] Write the minimal skill contract that forbids replacement and requires validation.
- [x] Run the structural test and confirm it passes.

### Task 2: Complete reference and template system

**Files:**
- Create: `skills/product-video-analysis/references/*.md`
- Create: `skills/product-video-analysis/templates/*.md`
- Create: `skills/product-video-analysis/templates/final-report-schema.json`
- Create: `skills/product-video-analysis/examples/onepay-example.md`

**Interfaces:**
- Produces: 25-module report contract and shot-level animation fields consumed by the validator.

- [x] Define all 25 modules with minimum evidence.
- [x] Define animation terminology, easing, sound, strategy, PDF, and evidence standards.
- [x] Define shot and animation templates.
- [x] Add a condensed worked example with Verified/Observed/Estimated/Inferred separation.

### Task 3: Report validator with TDD

**Files:**
- Create: `skills/product-video-analysis/scripts/validate_report.py`
- Create: `tests/fixtures/complete_report.json`
- Create: `tests/fixtures/incomplete_report.json`
- Test: `tests/test_validate_report.py`

**Interfaces:**
- Produces: `validate(data: dict) -> list[str]` and CLI exit status.

- [x] Write tests proving incomplete reports fail for missing modules, animation fields, evidence labels, and PDF QA.
- [x] Run tests and observe failure before implementation.
- [x] Implement minimal standard-library validation.
- [x] Run tests and confirm they pass.

### Task 4: Frame and audio evidence scripts with TDD

**Files:**
- Create: `skills/product-video-analysis/scripts/frame_extraction.py`
- Create: `skills/product-video-analysis/scripts/audio_analysis.py`
- Test: `tests/test_frame_extraction.py`
- Test: `tests/test_audio_analysis.py`

**Interfaces:**
- Produces frame manifests and audio-analysis JSON.

- [x] Generate a synthetic two-scene test video and 120 BPM click track.
- [x] Write tests for metadata, sample extraction, scene candidates, transients, and BPM candidates.
- [x] Implement standard-library wrappers around FFmpeg/FFprobe and signal analysis.
- [x] Run tests and confirm they pass.

### Task 5: Documentation, Codex layer, and CI

**Files:**
- Create: `README.md`
- Create: `codex/*`
- Create: `docs/methodology.md`
- Create: `.github/workflows/ci.yml`
- Create: `LICENSE`

**Interfaces:**
- Produces installation, execution, testing, and publication documentation.

- [x] Document current `npx skills add` installation commands.
- [x] Add Codex wrappers that execute installed canonical scripts.
- [x] Add CI for unittest and fixture validation.
- [x] Add MIT license and owner-maintained scope.

### Task 6: Final verification and packaging

**Files:**
- Test: all repository files

**Interfaces:**
- Produces: a clean Git repository and distributable ZIP.

- [x] Run `python -m unittest discover -s tests -v`.
- [x] Run `python tests/run-validation.py`.
- [x] Validate skill frontmatter and file references.
- [x] Initialize Git, commit all files, and create a ZIP artifact.
- [ ] Publish to `zhanziyang/product-video-analysis-skill` when an empty GitHub repository is available. The current GitHub connector can write to existing repositories but does not expose repository creation.
