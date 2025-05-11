# oralsharpdev：本地测试消息删除与更新接口

该目录包含对 `dify` 后端新增的两个 API 接口的本地测试脚本：

- 删除指定消息：`DELETE /messages/<message_id>`
- 更新指定消息：`PUT /messages/<message_id>`

## 📁 文件结构说明

- `test_message_api.py`: 使用 `requests` 库测试删除与更新接口的本地脚本
- `README.md`: 本地测试与部署说明（当前文件）

## 🧪 本地测试方法

1. 确保 `dify` 项目在本地正常运行，监听在默认端口 5000；
2. 替换 `test_message_api.py` 中的 `YOUR_APP_TOKEN` 与 `message_id`；
3. 执行测试脚本：

```bash
python test_message_api.py
