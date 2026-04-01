# Lab1 脚本中的 Python 模块说明

下文按「标准库」与「需单独安装的第三方包」分类，说明各模块在本实验里的典型用途。

---

## 一、标准库（Python 自带，无需 `pip install`）

### `glob`

- **作用**：用通配符（如 `*.txt`）在目录中查找匹配的文件路径，返回路径字符串列表。
- **在本实验中的用处**：`lab1_2025_IR_build_index.py` 里用来列出某目录下所有待建索引的文本文件，便于批量处理。

### `json`

- **作用**：读写 JSON 格式数据；可把 Python 字典/列表序列化成字符串写入文件，或从文件读回成 Python 对象。
- **在本实验中的用处**：
  - `build_index`：把倒排索引（字典等结构）**保存**为 `.json` 文件；
  - `search_inverted_index`：从磁盘**加载**已保存的倒排索引。

### `sys`

- **作用**：与 Python 解释器交互，常用 `sys.argv` 读取命令行参数、`sys.exit()` 退出程序等。
- **在本实验中的用处**：从命令行读取「数据目录路径」或「索引 JSON 路径」等，使脚本不必把路径写死在代码里。

### `collections` → `defaultdict`

- **作用**：`defaultdict` 是一种字典：访问**尚未存在**的键时，会自动用工厂函数（如 `set`、`list`）生成默认值，避免手写 `if key not in d`。
- **在本实验中的用处**：构建倒排索引时，常把「词 → 出现该词的文档 ID 集合/列表」存成 `defaultdict(set)` 或类似结构，简化「向某词追加文档 ID」的写法。

### `os`

- **作用**：操作系统相关接口，如创建目录、拼接路径、环境变量等。
- **在本实验中的用处**：`lab1_2025_IR_get_files.py` 里用 `os.makedirs(..., exist_ok=True)` **创建**存放 Reuters 导出文本的文件夹（若已存在则不报错）。

---

## 二、第三方包：NLTK（Natural Language Toolkit）

安装示例：

```bash
pip install nltk
```

首次使用语料或分词器前，通常还需要在 Python 里下载数据，例如：

```python
import nltk
nltk.download('punkt')      # word_tokenize 需要
nltk.download('reuters')    # Reuters 语料（get_files 脚本）
```

### `nltk.tokenize` → `word_tokenize`

- **作用**：把英文（等语言）**字符串切成词元（tokens）**，例如按标点、空格切分，并处理部分缩写等，比简单 `split()` 更符合 NLP 习惯。
- **在本实验中的用处**：`lab1_2025_IR_build_index.py` 中对每篇文档正文分词，再小写化后写入倒排索引的「词 → 文档 ID」结构。

### `nltk.corpus` → `reuters`

- **作用**：提供 **Reuters-21578** 新闻语料的访问接口，可按文档 ID 取**原始文本**等。
- **在本实验中的用处**：`lab1_2025_IR_get_files.py` 中从 NLTK 内置语料读出各篇报道，再**逐篇写入**你本地 `./reuters` 目录下的 `.txt` 文件，供后续建索引使用。

---

## 三、三个脚本与模块对应关系（速查）

| 脚本 | 用到的模块 |
|------|------------|
| `lab1_2025_IR_get_files.py` | `os`，`nltk.corpus.reuters` |
| `lab1_2025_IR_build_index.py` | `glob`，`json`，`sys`，`collections.defaultdict`，`nltk.tokenize.word_tokenize` |
| `lab1_2025_IR_search_inverted_index.py` | `json`，`sys` |

---

**说明**：上文中的「用处」与实验代码中的 TODO 注释一致，描述的是课程设计意图；你实现具体函数时，以实验 PDF 要求为准。
