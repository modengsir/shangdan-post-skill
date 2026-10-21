#!/usr/bin/env python3
"""新建一单的脚手架：在 campaigns/<slug>/ 下按模板生成五个工作文件。

用法：
    python3 scripts/new_campaign.py <slug> [--brand 品牌名] [--root 目录]

slug 只用小写字母、数字和连字符，如 my-first-deal。纯标准库，无依赖。
"""
import argparse
import datetime
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

FILES = [
    ("templates/brief_intake.md", "01-brief-intake.md"),
    ("templates/five_questions.md", "02-five-questions.md"),
    ("templates/outline.md", "03-outline.md"),
    (None, "04-post.md"),  # 成稿空文件，助理按大纲写
    ("templates/case_retro.md", "05-retro.md"),
]


def main() -> int:
    ap = argparse.ArgumentParser(description="新建一单商单工作目录")
    ap.add_argument("slug", help="单号 slug，如 my-first-deal")
    ap.add_argument("--brand", default="", help="品牌名（写进文件标题）")
    ap.add_argument("--root", default=str(REPO / "campaigns"), help="campaigns 根目录")
    args = ap.parse_args()

    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", args.slug):
        print("slug 只允许小写字母、数字、连字符，且以字母/数字开头", file=sys.stderr)
        return 2

    dest = Path(args.root) / args.slug
    if dest.exists():
        print(f"已存在，未覆盖：{dest}", file=sys.stderr)
        return 1
    dest.mkdir(parents=True)

    today = datetime.date.today().isoformat()
    for src, name in FILES:
        target = dest / name
        if src is None:
            target.write_text(f"# 成稿 · {args.slug}\n\n", encoding="utf-8")
            continue
        text = (REPO / src).read_text(encoding="utf-8")
        text = text.replace("{{slug}}", args.slug).replace("{{date}}", today)
        if args.brand:
            text = text.replace("品牌 / 产品：", f"品牌 / 产品：{args.brand}", 1)
        target.write_text(text, encoding="utf-8")

    print(f"已创建：{dest}")
    for _, name in FILES:
        print(f"  - {name}")
    print("下一步：把 Brief 原件放进该目录，然后对助理说「用商单 Skill 走这一单」。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
