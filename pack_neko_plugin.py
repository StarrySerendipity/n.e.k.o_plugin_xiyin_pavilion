"""
打包汐音阁插件为 .neko-plugin 格式
"""
import os
import shutil
try:
    import tomllib
except ImportError:
    import tomli as tomllib
from pathlib import Path

# 读取 plugin.toml
with open("plugin.toml", "rb") as f:
    meta = tomllib.load(f)

plugin_id = meta["plugin"]["id"]
version = meta["plugin"]["version"]
package_name = f"{plugin_id}.neko-plugin"

print(f"开始打包插件: {plugin_id} v{version}")

# 创建临时打包目录
pack_dir = Path("_pack_temp")
if pack_dir.exists():
    shutil.rmtree(pack_dir)
pack_dir.mkdir()

# 复制插件文件
shutil.copytree("plugins", pack_dir / "plugins")
shutil.copy2("plugin.toml", pack_dir / "plugin.toml")

# 创建 manifest.toml
manifest_content = f"""schema_version = "1.0"
package_type = "plugin"
id = "{plugin_id}"
package_name = "汐音阁"
version = "{version}"
package_description = "音乐推送插件，支持本地上传、在线链接、定时任务队列"
"""

with open(pack_dir / "manifest.toml", "w", encoding="utf-8") as f:
    f.write(manifest_content)

# 创建 metadata.toml
metadata_content = f"""id = "{plugin_id}"
version = "{version}"
name = "汐音阁"
description = "音乐推送插件，支持本地上传、在线链接、定时任务队列"
author = "N.E.K.O"
tags = ["music", "audio", "push", "scheduler"]
"""

with open(pack_dir / "metadata.toml", "w", encoding="utf-8") as f:
    f.write(metadata_content)

# 打包为 zip
output_file = Path(package_name)
if output_file.exists():
    output_file.unlink()

shutil.make_archive(plugin_id, "zip", pack_dir)
shutil.move(f"{plugin_id}.zip", package_name)

# 清理临时目录
shutil.rmtree(pack_dir)

print(f"打包完成: {package_name}")
print(f"文件大小: {output_file.stat().st_size} 字节")
