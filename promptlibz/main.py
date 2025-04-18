from llama_index.core import PromptTemplate
from enum import Enum
from typing import Any


class TemplateType(Enum):
    ANALYZE = 'analyze_template'
    CANVAS = 'canvas_template'
    SUMMARY = 'summary_template'
    PANDAS = "pandas_template"
    GITHUB = "github_template"
    SIMPLEPY = "py_simple_template"
    SIMPLEPY2 = "py_simple_template2"
    CREATETMP = "create_template"
    TEMP2CODE = "template2code_template"





class TemplateFactory:
    def __new__(cls, template_type: TemplateType) -> PromptTemplate:
        assert template_type.value in [item.value for item in TemplateType]
        template = None

        if template_type.value == 'analyze_template':

            template = """
            让我们一步步从用户的模糊需求中分析出明确且具体的需求步骤：

            第一步：提取用户表述中的关键词和重点内容。
            第二步：将关键词和重点内容转化成具体的步骤和需求。
            第三步：复核步骤和需求确保其明确具体且无二义性。
            第四步：将上述步骤和需求整理成明确的需求描述。

            用户需求表述：
            ---
            {user_statement}
            ---

            问题：请将上述用户需求表述转化为明确的需求描述。
            """

        elif template_type.value == 'canvas_template':

            template = """
            我希望你充当一个格式转换器, 按照下面的格式进行转换:
            我会输入一个API文档给你, 你应该按照以下规则进行转化, 我也会给你一些例子作为参考

            规则:
            ---
            颜色:
                函数:"4"
                类:"3"
                异步函数:"5"
                属性: "6"
            不同颜色的连线的含义
                执行该函数从而返回该类: "4"
                A类继承B类: 无
            ---


            例子:
            ---
            转换内容:

            Launcher
            pyppeteer.launcher.launch(options: dict = None, **kwargs) → pyppeteer.browser.Browser[source]
            Start chrome process and return Browser.

            This function is a shortcut to Launcher(options, **kwargs).launch().

            Available options are:

            ignoreHTTPSErrors (bool): Whether to ignore HTTPS errors. Defaults to False.
            headless (bool): Whether to run browser in headless mode. Defaults to True unless appMode or devtools options is True.
            executablePath (str): Path to a Chromium or Chrome executable to run instead of default bundled Chromium.
            slowMo (int|float): Slow down pyppeteer operations by the specified amount of milliseconds.
            args (List[str]): Additional arguments (flags) to pass to the browser process.
            ignoreDefaultArgs (bool): Do not use pyppeteer’s default args. This is dangerous option; use with care.
            handleSIGINT (bool): Close the browser process on Ctrl+C. Defaults to True.
            handleSIGTERM (bool): Close the browser process on SIGTERM. Defaults to True.
            handleSIGHUP (bool): Close the browser process on SIGHUP. Defaults to True.
            dumpio (bool): Whether to pipe the browser process stdout and stderr into process.stdout and process.stderr. Defaults to False.
            userDataDir (str): Path to a user data directory.
            env (dict): Specify environment variables that will be visible to the browser. Defaults to same as python process.
            devtools (bool): Whether to auto-open a DevTools panel for each tab. If this option is True, the headless option will be set False.
            logLevel (int|str): Log level to print logs. Defaults to same as the root logger.
            autoClose (bool): Automatically close browser process when script completed. Defaults to True.
            loop (asyncio.AbstractEventLoop): Event loop (experimental).
            appMode (bool): Deprecated.
            Note
            Pyppeteer can also be used to control the Chrome browser, but it works best with the version of Chromium it is bundled with. There is no guarantee it will work with any other version. Use executablePath option with extreme caution.
            pyppeteer.launcher.connect(options: dict = None, **kwargs) → pyppeteer.browser.Browser[source]
            Connect to the existing chrome.

            browserWSEndpoint option is necessary to connect to the chrome. The format is ws://${host}:${port}/devtools/browser/<id>. This value can get by wsEndpoint.

            Available options are:

            browserWSEndpoint (str): A browser websocket endpoint to connect to. (required)
            ignoreHTTPSErrors (bool): Whether to ignore HTTPS errors. Defaults to False.
            slowMo (int|float): Slow down pyppeteer’s by the specified amount of milliseconds.
            logLevel (int|str): Log level to print logs. Defaults to same as the root logger.
            loop (asyncio.AbstractEventLoop): Event loop (experimental).
            pyppeteer.launcher.executablePath() → str[source]
            Get executable path of default chrome.

            Browser Class
            class pyppeteer.browser.Browser(connection: pyppeteer.connection.Connection, contextIds: List[str], ignoreHTTPSErrors: bool, setDefaultViewport: bool, process: Optional[subprocess.Popen] = None, closeCallback: Callable[[], Awaitable[None]] = None, **kwargs)[source]
            Bases: pyee.EventEmitter

            Browser class.

            A Browser object is created when pyppeteer connects to chrome, either through launch() or connect().

            browserContexts
            Return a list of all open browser contexts.

            In a newly created browser, this will return a single instance of [BrowserContext]

            coroutine close() → None[source]
            Close connections and terminate browser process.

            coroutine createIncogniteBrowserContext() → pyppeteer.browser.BrowserContext[source]
            [Deprecated] Miss spelled method.

            Use createIncognitoBrowserContext() method instead.

            coroutine createIncognitoBrowserContext() → pyppeteer.browser.BrowserContext[source]
            Create a new incognito browser context.

            This won’t share cookies/cache with other browser contexts.

            browser = await launch()
            # Create a new incognito browser context.
            context = await browser.createIncognitoBrowserContext()
            # Create a new page in a pristine context.
            page = await context.newPage()
            # Do stuff
            await page.goto('https://example.com')
            ...
            coroutine disconnect() → None[source]
            Disconnect browser.

            coroutine newPage() → pyppeteer.page.Page[source]
            Make new page on this browser and return its object.

            coroutine pages() → List[pyppeteer.page.Page][source]
            Get all pages of this browser.

            Non visible pages, such as "background_page", will not be listed here. You can find then using pyppeteer.target.Target.page().

            process
            Return process of this browser.

            If browser instance is created by pyppeteer.launcher.connect(), return None.

            targets() → List[pyppeteer.target.Target][source]
            Get a list of all active targets inside the browser.

            In case of multiple browser contexts, the method will return a list with all the targets in all browser contexts.

            coroutine userAgent() → str[source]
            Return browser’s original user agent.

            Note
            Pages can override browser user agent with pyppeteer.page.Page.setUserAgent().
            coroutine version() → str[source]
            Get version of the browser.

            wsEndpoint
            Return websocket end point url.

            转换结果:

            '{\n  "edges": [\n    {\n      "fromNode": "657303b566ee6e2e",\n      "fromSide": "right",\n      "id": "2efc620dbe3c1331",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "54bff08a116e4a49",\n      "toSide": "left"\n    },\n    {\n      "fromNode": "54bff08a116e4a49",\n      "fromSide": "right",\n      "id": "a82325822bd67fb6",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "c67c993c745b37e0",\n      "toSide": "left"\n    },\n    {\n      "fromNode": "54bff08a116e4a49",\n      "fromSide": "right",\n      "id": "5641488c54221b63",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "bec0d8c67dac720b",\n      "toSide": "left"\n    },\n    {\n      "color": "4",\n      "fromNode": "c67c993c745b37e0",\n      "fromSide": "right",\n      "id": "c9389dd86f409516",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "3180d2a3fa2dfe4d",\n      "toSide": "top"\n    },\n    {\n      "color": "4",\n      "fromNode": "bec0d8c67dac720b",\n      "fromSide": "right",\n      "id": "8b46760ca9aafff8",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "3180d2a3fa2dfe4d",\n      "toSide": "top"\n    },\n    {\n      "fromNode": "cac3905b5dbd7aec",\n      "fromSide": "right",\n      "id": "6930dd6efcfe22c5",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "3180d2a3fa2dfe4d",\n      "toSide": "left"\n    },\n    {\n      "color": "4",\n      "fromNode": "ffb5f39dcb1d0035",\n      "fromSide": "right",\n      "id": "49590c97cf2bce72",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "87901b15f70c5419",\n      "toSide": "left"\n    },\n    {\n      "fromNode": "3180d2a3fa2dfe4d",\n      "fromSide": "right",\n      "id": "b3263c6139ae433d",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "ffb5f39dcb1d0035",\n      "toSide": "left"\n    },\n    {\n      "fromNode": "3180d2a3fa2dfe4d",\n      "fromSide": "right",\n      "id": "6ea16715faac92f3",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "ef50ac442c163ad3",\n      "toSide": "left"\n    },\n    {\n      "fromNode": "3180d2a3fa2dfe4d",\n      "fromSide": "right",\n      "id": "0f78fc09750b21ba",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "d5672e020eb1ab01",\n      "toSide": "left"\n    },\n    {\n      "fromNode": "3180d2a3fa2dfe4d",\n      "fromSide": "right",\n      "id": "3e4ce809d293f027",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "1d3055f1f01bfd0d",\n      "toSide": "left"\n    },\n    {\n      "color": "4",\n      "fromNode": "ef50ac442c163ad3",\n      "fromSide": "right",\n      "id": "45a37e74ada80dcb",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "94fc5d8fb8d9206e",\n      "toSide": "left"\n    },\n    {\n      "color": "4",\n      "fromNode": "d5672e020eb1ab01",\n      "fromSide": "right",\n      "id": "113bd8fc1c6dfc8c",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "94fc5d8fb8d9206e",\n      "toSide": "left"\n    },\n    {\n      "color": "4",\n      "fromNode": "a6ec1edaffecbedb",\n      "fromSide": "right",\n      "id": "a7eadc89526932ec",\n      "label": "list",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "19d350c22cff8b8a",\n      "toSide": "left"\n    },\n    {\n      "color": "4",\n      "fromNode": "e6a1b690b5f05804",\n      "fromSide": "right",\n      "id": "51bdecc33602917b",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "19d350c22cff8b8a",\n      "toSide": "left"\n    },\n    {\n      "color": "4",\n      "fromNode": "2272171aa68c4319",\n      "fromSide": "right",\n      "id": "0e9cf235d823c638",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "87901b15f70c5419",\n      "toSide": "left"\n    },\n    {\n      "fromNode": "3180d2a3fa2dfe4d",\n      "fromSide": "right",\n      "id": "1a2ed793c302f815",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "d9b66e51bb3668bc",\n      "toSide": "left"\n    },\n    {\n      "color": "4",\n      "fromNode": "d9b66e51bb3668bc",\n      "fromSide": "right",\n      "id": "0193fc32e449697d",\n      "label": "list",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "b748946b6c3b7462",\n      "toSide": "left"\n    },\n    {\n      "fromNode": "3180d2a3fa2dfe4d",\n      "fromSide": "right",\n      "id": "4aa36fdb75140c7d",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "9a93a0822a5119ec",\n      "toSide": "left"\n    },\n    {\n      "fromNode": "3ef85b796461c349",\n      "fromSide": "right",\n      "id": "24100ebc6df82e9b",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "ebf3fbce8a41db9d",\n      "toSide": "left"\n    },\n    {\n      "fromNode": "211830253acc4b69",\n      "fromSide": "right",\n      "id": "e82dd6b8930dc31c",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "ebf3fbce8a41db9d",\n      "toSide": "left"\n    },\n    {\n      "fromNode": "3180d2a3fa2dfe4d",\n      "fromSide": "right",\n      "id": "fc7ef600565522fc",\n      "styleAttributes": {\n        "pathfindingMethod": "a-star"\n      },\n      "toNode": "bc5e5afb1d2202d6",\n      "toSide": "left"\n    }\n  ],\n  "nodes": [\n    {\n      "height": 60,\n      "id": "54bff08a116e4a49",\n      "styleAttributes": {\n      },\n      "text": "launcher",\n      "type": "text",\n      "width": 260,\n      "x": -390,\n      "y": -650\n    },\n    {\n      "color": "5",\n      "height": 60,\n      "id": "c67c993c745b37e0",\n      "styleAttributes": {\n      },\n      "text": "launch",\n      "type": "text",\n      "width": 260,\n      "x": -30,\n      "y": -560\n    },\n    {\n      "height": 60,\n      "id": "657303b566ee6e2e",\n      "styleAttributes": {\n      },\n      "text": "pyppeteer",\n      "type": "text",\n      "width": 260,\n      "x": -700,\n      "y": -500\n    },\n    {\n      "color": "5",\n      "height": 60,\n      "id": "bec0d8c67dac720b",\n      "styleAttributes": {\n      },\n      "text": "connect",\n      "type": "text",\n      "width": 260,\n      "x": -30,\n      "y": -680\n    },\n    {\n      "color": "3",\n      "height": 60,\n      "id": "cac3905b5dbd7aec",\n      "styleAttributes": {\n      },\n      "text": "EventEmitter",\n      "type": "text",\n      "width": 260,\n      "x": -660,\n      "y": -40\n    },\n    {\n      "color": "3",\n      "height": 60,\n      "id": "3180d2a3fa2dfe4d",\n      "styleAttributes": {\n      },\n      "text": "Browser",\n      "type": "text",\n      "width": 260,\n      "x": -350,\n      "y": -220\n    },\n    {\n      "color": "5",\n      "height": 60,\n      "id": "2272171aa68c4319",\n      "styleAttributes": {\n      },\n      "text": "disconnect",\n      "type": "text",\n      "width": 260,\n      "x": -30,\n      "y": 240\n    },\n    {\n      "color": "5",\n      "height": 60,\n      "id": "e6a1b690b5f05804",\n      "styleAttributes": {\n      },\n      "text": "newPage",\n      "type": "text",\n      "width": 260,\n      "x": -30,\n      "y": 340\n    },\n    {\n      "color": "5",\n      "height": 60,\n      "id": "a6ec1edaffecbedb",\n      "styleAttributes": {\n      },\n      "text": "pages",\n      "type": "text",\n      "width": 260,\n      "x": -30,\n      "y": 450\n    },\n    {\n      "color": "5",\n      "height": 60,\n      "id": "ef50ac442c163ad3",\n      "styleAttributes": {\n      },\n      "text": "createIncogniteBrowserContext()",\n      "type": "text",\n      "width": 260,\n      "x": -30,\n      "y": -60\n    },\n    {\n      "color": "5",\n      "height": 60,\n      "id": "d5672e020eb1ab01",\n      "styleAttributes": {\n      },\n      "text": "createIncognitoBrowserContext()",\n      "type": "text",\n      "width": 260,\n      "x": -30,\n      "y": 60\n    },\n    {\n      "color": "4",\n      "height": 60,\n      "id": "d9b66e51bb3668bc",\n      "styleAttributes": {\n      },\n      "text": "targets()",\n      "type": "text",\n      "width": 260,\n      "x": -30,\n      "y": 150\n    },\n    {\n      "color": "6",\n      "height": 60,\n      "id": "1d3055f1f01bfd0d",\n      "styleAttributes": {\n      },\n      "text": "browserContexts",\n      "type": "text",\n      "width": 260,\n      "x": -30,\n      "y": -240\n    },\n    {\n      "color": "5",\n      "height": 60,\n      "id": "ffb5f39dcb1d0035",\n      "styleAttributes": {\n      },\n      "text": "close",\n      "type": "text",\n      "width": 260,\n      "x": -30,\n      "y": -160\n    },\n    {\n      "color": "6",\n      "height": 60,\n      "id": "9a93a0822a5119ec",\n      "styleAttributes": {\n      },\n      "text": "process",\n      "type": "text",\n      "width": 260,\n      "x": -30,\n      "y": -310\n    },\n    {\n      "color": "3",\n      "height": 60,\n      "id": "94fc5d8fb8d9206e",\n      "styleAttributes": {\n      },\n      "text": "BrowserContext",\n      "type": "text",\n      "width": 260,\n      "x": 380,\n      "y": 10\n    },\n    {\n      "color": "3",\n      "height": 60,\n      "id": "b748946b6c3b7462",\n      "styleAttributes": {\n      },\n      "text": "Target",\n      "type": "text",\n      "width": 260,\n      "x": 380,\n      "y": 160\n    },\n    {\n      "color": "3",\n      "height": 60,\n      "id": "19d350c22cff8b8a",\n      "styleAttributes": {\n      },\n      "text": "Page",\n      "type": "text",\n      "width": 260,\n      "x": 380,\n      "y": 310\n    },\n    {\n      "height": 60,\n      "id": "87901b15f70c5419",\n      "styleAttributes": {\n      },\n      "text": "",\n      "type": "text",\n      "width": 260,\n      "x": 380,\n      "y": -90\n    },\n    {\n      "height": 60,\n      "id": "ebf3fbce8a41db9d",\n      "styleAttributes": {\n      },\n      "text": "str",\n      "type": "text",\n      "width": 260,\n      "x": 400,\n      "y": 460\n    },\n    {\n      "color": "5",\n      "height": 60,\n      "id": "211830253acc4b69",\n      "styleAttributes": {\n      },\n      "text": "version",\n      "type": "text",\n      "width": 260,\n      "x": -30,\n      "y": 680\n    },\n    {\n      "color": "5",\n      "height": 60,\n      "id": "3ef85b796461c349",\n      "styleAttributes": {\n      },\n      "text": "userAgent",\n      "type": "text",\n      "width": 260,\n      "x": -30,\n      "y": 560\n    },\n    {\n      "color": "6",\n      "height": 60,\n      "id": "bc5e5afb1d2202d6",\n      "styleAttributes": {\n      },\n      "text": "wsEndpoint",\n      "type": "text",\n      "width": 260,\n      "x": -30,\n      "y": -380\n    }\n  ]\n}'

            ---


            接下来, 帮我转换这个API文档内容:

            """


        elif template_type.value == 'summary_template':
  
            template  = """
            让我们一步步从下列对话文本中抽取有用信息做总结:

            第一步: 思考哪些信息是有价值的? 并列举出来.
            第二步: 思考内容是否可以提炼, 同时保证重要信息.
            第三步: 分别用偏向理性的,偏向数据的,偏向感性的三种不同风格,将信息汇总并编撰笔记.内容要详实一些.
            第四步: 将三种笔记结合其优点进行汇总成最终笔记


            对话文本:
            ---
            {chat_history}
            ---
            问题：请将上述对话文本汇总成笔记.
            """

        elif template_type.value == 'pandas_template':
            template  = """
            你是一个pandas的大师, 你需要根据你看到的df.sample(4) 的数据样例, 和用户的诉求, 编写对应的操作python代码来实现功能.
            假设你可以直接操作名为df 的变量,它就是你看到的DataFrame.
            你可以将你的输出打包成函数,这样用户更方便使用

            数据样例(df.sample(4)):
            ---
            {data_sample}
            ---
            数据格式(df.info()):
            ---
            {data_info}
            ---
            用户诉求:
            {prompt}
            ---
            输出python程序:
            """

        elif template_type.value == 'github_template':


            # 定义提示模板字符串
            template = """
            您是一个Python工程师, 现在我希望你可以按照以下的git diff 的输出结果,来编写一个
            标准的git commit 提交信息.
            编写的提交信息,应该要结合用户的表达和git commit 标准格式


            git commit 标准格式:
            ---
            1. commitizen
            AngularJS在 github上 的提交记录被业内许多人认可，逐渐被大家引用。
            commit 格式规范
            js 代码解读复制代码<type类型>(<scope 可选作用域>): <subject 描述>
            <BLANK LINE>
            <body 可选的正文>
            <BLANK LINE>
            <footer 可选的脚注>

            大致主要分为三个部分（每个部分中间用空行分割）：

            标题行: 必填, 描述主要修改类型和内容
            主题内容: 描述为什么修改, 做了什么样的修改, 以及开发的思路等等
            页脚注释: 可以写注释，BUG 号链接 或 Closed Issues


            标题行中的type（必须）：commit 类型，只能填写如下类型：


            feat: 新功能、新特性
            fix: 修改 bug
            perf: 更改代码，性能优化
            refactor: 代码重构（重构，在不影响代码内部行为、功能下的代码修改）
            docs: 文档修改
            style: 代码格式修改, 注意不是 css 修改（例如分号修改）
            test: 测试用例新增、修改
            build: 影响项目构建或依赖项修改
            revert: 恢复上一次提交
            ci: 持续集成相关文件修改
            chore: 其他修改（不在上述类型中的修改）
            release: 发布新版本
            workflow: 工作流相关文件修改


            scope（可选）: 用于说明commit 影响的范围, 比如: global, common, route, component, utils, build...
            subject: commit 的简短概述，不超过50个字符。
            body: commit 具体修改内容, 可以分为多行。
            footer: 一些备注, 通常是 BREAKING CHANGE 或修复的 bug 的链接。

            例如如下示例：
            js 代码解读复制代码// 示例1 
            fix(global):修复checkbox不能复选的问题 
            // 示例2 
            fix(common): 修复头部区域logo问题

            js 代码解读复制代码// 示例1 
            feat: 添加资产管理模块

            增加资产列表、搜索。

            需求No.181 http://xxx.xxx.com/181。

            约定式提交规范
            内容来自(www.conventionalcommits.org/zh-hans/v1.…)

            每个提交都必须使用类型字段前缀，它由一个名词组成，诸如 feat 或 fix ，其后接一个可选的作用域字段，以及一个必要的冒号（英文半角）和空格。
            当一个提交为应用或类库实现了新特性时，必须使用 feat 类型。
            当一个提交为应用修复了 bug 时，必须使用 fix 类型。
            作用域字段可以跟随在类型字段后面。作用域必须是一个描述某部分代码的名词，并用圆括号包围，例如： fix(parser):
            描述字段必须紧接在类型/作用域前缀的空格之后。描述指的是对代码变更的简短总结，例如： fix: array parsing issue when multiple spaces were contained in string.
            在简短描述之后，可以编写更长的提交正文，为代码变更提供额外的上下文信息。正文必须起始于描述字段结束的一个空行后。
            在正文结束的一个空行之后，可以编写一行或多行脚注。脚注必须包含关于提交的元信息，例如：关联的合并请求、Reviewer、破坏性变更，每条元信息一行。
            破坏性变更必须标示在正文区域最开始处，或脚注区域中某一行的开始。一个破坏性变更必须包含大写的文本 BREAKING CHANGE，后面紧跟冒号和空格。
            在 BREAKING CHANGE: 之后必须提供描述，以描述对 API 的变更。例如： BREAKING CHANGE: environment variables now take precedence over config files.
            在提交说明中，可以使用 feat 和 fix 之外的类型。
            工具的实现必须不区分大小写地解析构成约定式提交的信息单元，只有 BREAKING CHANGE 必须是大写的。
            可以在类型/作用域前缀之后，: 之前，附加 ! 字符，以进一步提醒注意破坏性变更。当有 ! 前缀时，正文或脚注内必须包含 BREAKING CHANGE: description

            ---
            git diff info:
            ---
            {git_diff}
            ---

            用户的表达:
            ---
            {prompt}
            ---

            """

        elif template_type.value == 'py_simple_template':
            template = """
            您是一个Python工程师, 现在我希望你可以负责 {py_name} 的代码维护和更新工作

            您应该在尽可能少的改动代码的前提下, 满足新功能或改动诉求.

            {py_name} 介绍:
            ---
            {py_name} 的主要职能是:       {duty}
            {py_name} 在整个工程中的位置是: {location}
            {py_name} 与其他py的交互情况:  {interaction}

            ---

            {py_name} 全部代码:
            ```python
            {py_content}
            ```

            用户的代码片段和要求:
            ---
            {prompt}
            ---
            输出新的build函数:
            """

        elif template_type.value == 'py_simple_template2':
            template = """
            你是一个python工程师, 这里有两段代码
            一段是最初的代码, 有着可以执行的完整性.
            第二段是 大模型编写的代码，其中由于大模型的注意力有限，而忽略或省去了一部分内容，现在我希望你将 第二段代码加入第一段代码
            第一段代码:
            ---
            ```python
            {code1}
            ```
            ---

            第二段代码
            ---
            ```python
            {code2}
            ```
            ---
            """

        elif template_type.value == 'create_template':
            template  = """
            请帮我根据以下代码生成一个对应的代码模版

            例子1
            ```python
            {case1}
            ```

            例子2
            ```python
            {case2}
            ```

            模版:
            """

        elif template_type.value == 'template2code_template':
            template = """
            你是一个Python工程师, 我希望你可以根据模版,将用户提供的一些代码碎片整合成模版的形式

            代码模版:
            ```python
            {python_code_template}
            ```

            用户的代码片段和要求:
            ---
            {prompt}
            ---
            输出新的build函数:
            """

        elif template_type.value == 'pandas3_template':
            pass
        elif template_type.value == 'pandas4_template':
            pass


        else:
            raise Exception('Unknown enum_type')

        return PromptTemplate(template=template)





from llama_index.core import PromptTemplate
from quickuse.llms import get_llm

template = """
让我们一步步从用户的模糊需求中分析出明确且具体的需求步骤：

第一步：提取用户表述中的关键词和重点内容。
第二步：将关键词和重点内容转化成具体的步骤和需求。
第三步：复核步骤和需求确保其明确具体且无二义性。
第四步：将上述步骤和需求整理成明确的需求描述。

用户需求表述：
---
{user_statement}
---

问题：请将上述用户需求表述转化为明确的需求描述。
"""

def analyze(multi_line_input):
    llm = get_llm()
    analyze_template = PromptTemplate(template=template)
    response = llm.complete(analyze_template.format(user_statement=multi_line_input))
    return response.text



if __name__ == "__main__":
    import sys
    multi_line_input = sys.stdin.read()
    print(analyze(multi_line_input))

import pandas as pd
from addict import Dict
import random
import json
import re
from llama_index.llms.openai import OpenAI
import os

class GetInfo():
    def __init__(self,canvas_file:str):
        self.canvas_file = canvas_file
        self.dicts = self.load(canvas_file)
        self.nodes = pd.DataFrame(self.dicts['nodes'])
        self.edges = pd.DataFrame(self.dicts['edges'])
        
    def load(self,folder):
        with open(folder,'r') as f:
            text = f.read()
        return json.loads(text)
    
    def clean_data_custom(self):
        self.edges_ = self.edges[['id','fromNode','fromSide','toNode','toSide']]
        self.nodes_ = self.nodes[['color','id','text']]

        return {"nodes":self.nodes_.to_dict(),
               "edges":self.edges_.to_dict()}
    
    def update_df_by(self,df1,df2):
        df1_ = df1.set_index('id', inplace=False)
        df2_ = df2.set_index('id', inplace=False)
        df1_.update(df2_)
        df1_.reset_index(inplace=True)
        return df1_
    
    def up_data_custom(self,x):
        nodes = pd.DataFrame(x['nodes'])
        edges = pd.DataFrame(x['edges'])
        self.nodes_updated = self.update_df_by(self.nodes,nodes)
        self.edges_updated = self.update_df_by(self.edges,edges)
        
        return {"nodes":list(self.nodes_updated.T.to_dict().values()),
                "edges":list(self.edges_updated.T.to_dict().values())
               }

def extract_json_code(text):
    pattern = r'```json([\s\S]*?)```'
    matches = re.findall(pattern, text)
    return matches

def clean_json(result):
    # 清洗 JSON 数据
    json_string = extract_json_code(result.text)[-1]
    cleaned_json = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', json_string)
    cleaned_json = cleaned_json.replace(' ','')
    return cleaned_json

def decodeJson(cleaned_json):
    try:
        parsed_dict = json.loads(cleaned_json, strict=False)
        print("JSON 解析成功！")
        # 打印解析后的字典
    except json.JSONDecodeError as e:
        print("JSON 解析失败:", e)
    return parsed_dict

templates = '''
please step by step:

基本介绍:
    这里有两幅图数据结构表示的工程图, 第一张是流程图,介绍了基本的工作流程, 第二张是施工图,具体描述了正在进行的工作和工作的状态
    
1 我希望你可以可以深入了解他们,并理解他们的含义.
2 根据施工图的颜色和描述等信息, 根据下列规则判断和操作
3 输出修改后的流程图



判断规则如下:
---
如果施工图中的nodes的颜色是4, 那么说明这个工作已经完成.
理解施工图中完成的工作和流程图中流程的对应关系, 将对应的流程图中的nodes 的颜色改为4
注意 输出的json格式不要有任何注释内容
---

流程图如下:
---
{flow}
---
施工图如下:
---
{work}
---

修改后的流程图:
'''
file_path = "/Users/zhaoxuefeng/本地文稿/百度空间/cloud/Obsidian/知识体系尝试/工作/事件看板"

llm = OpenAI(
    model="gpt-4o",
    api_key='sk-tQ17YaQSAvb6REf474A112Eb57064c5d9f6a9599F96a35A6',
    api_base='https://api.bianxieai.com/v1',
    temperature=0.1,
)

def main():
    flow_path = 'project-ChatWallet-beta.canvas'
    flow_path2= 'project-ChatWallet-beta2.canvas'
    work_path = 'project-ChatWallet-beta施工图.canvas'
    
    
    # flow_path = '测试11.canvas'
    # work_path = '测试11施工图.canvas'
    inf = GetInfo(os.path.join(file_path,flow_path))
    inf2 = GetInfo(os.path.join(file_path,work_path))

    flow = inf.clean_data_custom()
    work = inf2.clean_data_custom()
    print('start')
    print(templates.format(flow = flow, work = work),'<<<<<<<<<<')
    result = llm.complete(templates.format(flow = flow, work = work))
    print('output')
    print(result.text,'text')
    cleaned_json = clean_json(result)
    parsed_dict = decodeJson(cleaned_json)
    ens = inf.up_data_custom(parsed_dict)
    aac = json.dumps(ens)
    
    with open(os.path.join(file_path,flow_path2),'w') as f:
        f.write(aac)

if __name__ == "__main__":
    main()


from enum import Enum
from llama_index.core import PromptTemplate
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
from quickuse.tools.retools import extract_python_code
import os
import re
import json
import time

from enum import Enum
class Side(Enum):
    right = "right"
    left = "right"
    top = "top"
    bottom = "bottom"

class Edge:
    __slots__ = ['fromNode', 'fromSide', 'id','label', 'styleAttributes', 'toNode', 'toSide']

    def __init__(self, 
                 from_node: str, 
                 from_side: Side, 
                 id: str, 
                 style_attributes: dict,
                 label:str,
                 to_node: str, 
                 to_side: Side):
        self.fromNode = from_node
        self.fromSide = from_side.value
        self.id = id
        self.styleAttributes = style_attributes
        self.label = label
        self.toNode = to_node
        self.toSide = to_side.value

    def to_dict(self):
        return {attr: getattr(self, attr) for attr in self.__slots__}

class Node:
    __slots__ = ['height', 'width', 'x', 'y', 'id', 'type','text','styleAttributes']

    def __init__(self, 
                 height: int = 60, 
                 width: int = 260, 
                 x: str = 440, 
                 y: dict = 80, 
                 id: str='1', 
                 type = "text",
                 text: str = "开始",
                 styleAttributes:dict={}):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.id = id
        self.type = type
        self.text = text
        self.styleAttributes = styleAttributes

    def to_dict(self):
        return {attr: getattr(self, attr) for attr in self.__slots__}


# 全局配置
api_key = os.environ.get('OPENAI_API_KEY')

# 初始化 LLM 和 Embedding 模型
llm = OpenAI(
    model="gpt-4o",
    api_key='sk-tQ17YaQSAvb6REf474A112Eb57064c5d9f6a9599F96a35A6',
    api_base='https://api.bianxieai.com/v1',
    temperature=0.1,
)
embed_model = OpenAIEmbedding(api_key=api_key)
Settings.embed_model = embed_model
Settings.llm = llm


prompt = """
你是一个python工程师, 你负责将mermaid格式转化为特定的函数调用,函数的方式会在下方给出
你需要给出相关代码
注意:
不需要再次定义函数,只需要给出转化部分

函数说明:
---
class Side(Enum):
    right = "right"
    left = "right"
    top = "top"
    bottom = "bottom"
    
class Edge:
    __slots__ = ['fromNode', 'fromSide', 'id','label', 'styleAttributes', 'toNode', 'toSide']

    def __init__(self, 
                 from_node: str, 
                 from_side: Side, 
                 id: str, 
                 style_attributes: dict,
                 label:str,
                 to_node: str, 
                 to_side: Side):
        self.fromNode = from_node
        self.fromSide = from_side.value
        self.id = id
        self.styleAttributes = style_attributes
        self.label = label
        self.toNode = to_node
        self.toSide = to_side.value

    def to_dict(self):
        return {attr: getattr(self, attr) for attr in self.__slots__}

class Node:
    __slots__ = ['height', 'width', 'x', 'y', 'id', 'type','text','styleAttributes']

    def __init__(self, 
                 height: int = 60, 
                 width: int = 260, 
                 x: str = 440, 
                 y: dict = 80, 
                 id: str='1', 
                 type = "text",
                 text: str = "开始",
                 styleAttributes:dict={}):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.id = id
        self.type = type
        self.text = text
        self.styleAttributes = styleAttributes

    def to_dict(self):
        return {attr: getattr(self, attr) for attr in self.__slots__}

---

for example:

mermaid

```mermaid
graph TD
    A[开始] --> B[准备采访问题]
    B --> C[进行采访]
    C --> D{采访者回答是否满意?}
    D -->|是| E[记录回答]
    D -->|否| F[调整问题]
```

转化为:

```python
edges = [Edge(from_node="218966d3990f15f6", from_side=Side.bottom, id="905bbe317b954c36",label="是", style_attributes={"pathfindingMethod": None}, to_node="2823d50c24e7534d", to_side=Side.top).to_dict(),
         Edge(from_node="218966d3990f15f6", from_side=Side.bottom, id="42b4f715b308c43e",label="否", style_attributes={"pathfindingMethod": None}, to_node="cfd410b6ee11ba81", to_side=Side.top).to_dict(),
         Edge(from_node="de67d252e584c626", from_side=Side.bottom, id="f4a1354b4f865171",label=None, style_attributes={"pathfindingMethod": "square"}, to_node="a385eec25062ed45", to_side=Side.top).to_dict(),
         Edge(from_node="a385eec25062ed45", from_side=Side.bottom, id="84b6c9a22fb05ad1",label=None, style_attributes={"pathfindingMethod": "square"}, to_node="0cc873f796f38c97", to_side=Side.top).to_dict(),
         Edge(from_node="0cc873f796f38c97", from_side=Side.bottom, id="b4ec373818d7df5c",label=None, style_attributes={"pathfindingMethod": "square"}, to_node="218966d3990f15f6", to_side=Side.top).to_dict(),
        ]
nodes = [Node(id ="218966d3990f15f6",text="采访者回答是否满意",x=-280,y=120).to_dict(),
         Node(id ="2823d50c24e7534d",text="记录回答",x=-500,y=320).to_dict(),
         Node(id ="cfd410b6ee11ba81",text="调整问题",x=-20,y=320).to_dict(),
         Node(id ="de67d252e584c626",text="开始",x=-280,y=-300).to_dict(),
         Node(id ="a385eec25062ed45",text="准备采访问题",x=-280,y=-160).to_dict(),
         Node(id ="0cc873f796f38c97",text="进行采访",x=-280,y=-20).to_dict(),
]
```


start:
---

mermaid
{mermaid}

转化为:
"""



def main(mermaid:str,path:str):
    """
    mermaid
    path
    """
    prompt_temp = PromptTemplate(prompt)
    resp = llm.complete(prompt_temp.format(mermaid=mermaid))
    python_code_str = extract_python_code(resp.text)
    codes = "\n".join(python_code_str) 

    info = {"nodes":None,
            "edges":None}

    exec(codes, globals(), info)
    with open(path,'w') as f:
        f.write(json.dumps(info))
    return 'success'

if __name__ == "__main__":

    import sys
    mermaid = sys.stdin.read()
    path = f"/Users/zhaoxuefeng/本地文稿/百度空间/cloud/Obsidian/知识体系尝试/工作/事件看板/Create_AI_{str(time.time())[:-8]}.canvas"
    result = main(mermaid,path)
    print(result)


temp = PromptTemplate("""
你是一个架构设计师, 我们之间会根据一个主题做讨论, 你会维护并不断更新一个mermaid框架图代码,这也是你的最终产出.

你将分两步完成以下任务:
步骤一 收集信息:
    1 为让我们的主题收集相关信息, 或者相关的可能的技术站
    2 列出相关技术产的性质优势不足

步骤二 根据手里的信息修改mermaid框架图

mermaid框架图
```

```

主题:{topic}
""")