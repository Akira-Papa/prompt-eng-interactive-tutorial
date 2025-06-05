exercise_1_1_hint = """この演習の採点関数は、正確なアラビア数字「1」、「2」、「3」を含む回答を探しています。
Claudeに望むことをしてもらうには、単純にお願いするだけで済むことが多いです。"""

exercise_1_2_hint = """この演習の採点関数は、「soo」または「giggles」を含む回答を探しています。
これを解決する方法はたくさんあります。お願いするだけです！"""

exercise_2_1_hint ="""この演習の採点関数は、「hola」という単語を含む回答を探しています。
人間と話すときのように、Claudeにスペイン語で返答するよう求めてください。それだけです！"""

exercise_2_2_hint = """この演習の採点関数は、正確に「Michael Jordan」を探しています。
これを人間に依頼するとしたら、どのように頼みますか？他の言葉なしで返答？名前のみで他は何もなし？このアプローチにはいくつかの方法があります。"""

exercise_2_3_hint = """このセルの採点関数は、800語以上の回答を探しています。
LLMはまだ単語数を数えるのが得意ではないため、目標を上回る必要があるかもしれません。"""

exercise_3_1_hint = """この演習の採点関数は、「incorrect」または「not correct」という言葉を含む回答を探しています。
Claudeに数学問題をより良く解けるような役割を与えてください！"""

exercise_4_1_hint = """この演習の採点関数は、「haiku」と「pig」という言葉を含む解決策を探しています。
トピックを代入したい場所に正確に「{TOPIC}」というフレーズを含めることを忘れないでください。「TOPIC」変数の値を変更すると、Claudeが異なるトピックについて俳句を書くようになります。"""

exercise_4_2_hint = """この演習の採点関数は、「brown」という単語を含む回答を探しています。
「{QUESTION}」をXMLタグで囲むと、Claudeの回答がどのように変わりますか？"""

exercise_4_3_hint = """この演習の採点関数は、「brown」という単語を含む回答を探しています。
最も意味をなさない部分から始めて、一度に一つの単語または文字の部分を削除してみてください。一度に一つの単語ずつ実行することで、Claudeがどの程度解析・理解できるかも確認できます。"""

exercise_5_1_hint = """この演習の採点関数は、「Warrior」という単語を含む回答を探しています。
Claudeの声でより多くの言葉を書いて、Claudeが望む通りに行動するよう導いてください。例えば、「Stephen Curry is the best because」の代わりに、「Stephen Curry is the best and here are three reasons why. 1:」と書くことができます。"""

exercise_5_2_hint = """採点関数は、「cat」と「<haiku>」という単語を含む5行以上の回答を探しています。
シンプルに始めましょう。現在、プロンプトはClaudeに一つの俳句を求めています。それを変更して二つ（またはそれ以上）を求めることができます。フォーマットの問題が発生した場合は、Claudeに複数の俳句を書かせることができた後で、それを修正するようプロンプトを変更してください。"""

exercise_5_3_hint = """この演習の採点関数は、「tail」、「cat」、「<haiku>」という単語を含む回答を探しています。
この演習をいくつかのステップに分けると便利です。								
1.	Claudeが二つの詩を書くように初期プロンプトテンプレートを修正する。							
2.	詩のテーマについてClaudeに指示を与えるが、主題を直接書く（例：犬、猫など）代わりに、その主題を「{ANIMAL1}」と「{ANIMAL2}」というキーワードで置き換える。							
3.	プロンプトを実行し、変数代入を含む完全なプロンプトですべての単語が正しく代入されていることを確認する。そうでない場合は、{bracket}タグが正しくスペルされ、単一の山括弧で正しくフォーマットされていることを確認する。"""

exercise_6_1_hint = """この演習の採点関数は、正しい分類文字 + 閉じ括弧 + カテゴリ名の最初の文字（「C) B」や「B) B」など）を探しています。
この演習を段階的に進めましょう：										
1.	Claudeにどのカテゴリを使用したいかをどのように知らせますか？教えてください！使用したい四つのカテゴリをプロンプトに直接含めてください。簡単な分類のために括弧文字も含めてください。XMLタグを使ってプロンプトを整理し、カテゴリがどこで始まりどこで終わるかをClaudeに明確にしてください。									
2.	Claudeが分類のみで即座に答えるよう、余分なテキストを削減してください。文の始まりから単一の開き括弧まで何でも提供してClaudeに答えの最初の部分として括弧文字が欲しいことを知らせることから、前置きをスキップして分類のみが欲しいとClaudeに伝えることまで、いくつかの方法があります。
これらのテクニックの復習が必要な場合は第2章と第5章を参照してください。							
3.	Claudeはまだ間違って分類しているか、答える際にカテゴリ名を含めていない可能性があります。答えに完全なカテゴリ名を含めるようClaudeに指示してこれを修正してください。								
4.	Claudeが評価するメールを適切に代入できるよう、プロンプトテンプレートのどこかに{email}があることを確認してください。"""

exercise_6_1_solution = """
USER TURN
Please classify this email into the following categories: {email}

Do not include any extra words except the category.

<categories>
(A) Pre-sale question
(B) Broken or defective item
(C) Billing question
(D) Other (please explain)
</categories>

ASSISTANT TURN
(
"""

exercise_6_2_hint = """この演習の採点関数は、「<answer>B</answer>」のような<answer>タグで囲まれた正しい文字のみを探しています。正しい分類文字は上記の演習と同じです。
これを行う最も簡単な方法は、出力がどのように見えるかの例をClaudeに与えることです。例を<example></example>タグで囲むことを忘れないでください！また、Claudeの回答を何かで事前入力する場合、Claudeは実際にはそれを回答の一部として出力しないことを忘れないでください。"""

exercise_7_1_hint = """（求めているフォーマットで）Claudeのためにいくつかのサンプルメールを書いて分類する必要があります。これを行う方法は複数あります。以下にガイドラインをいくつか示します。										
1.	少なくとも二つのサンプルメールを作成してください。Claudeはすべてのカテゴリの例は必要なく、例は長くある必要もありません。より難しいと思われるカテゴリ（第6章演習1の最後で考えるよう求められたもの）の例があると便利です。XMLタグは例をプロンプトの他の部分から分離するのに役立ちますが、必須ではありません。									
2.	サンプル回答のフォーマットが、Claudeに使用してもらいたい正確なフォーマットになっていることを確認してください。そうすればClaudeもそのフォーマットを模倣できます。このフォーマットでは、Claudeの回答がカテゴリの文字で終わるようにします。{email}プレースホルダーを配置する場所では、サンプルメールと同じようにフォーマットされていることを確認してください。									
3.	プロンプト自体にカテゴリがリストされていることと、代入用のプレースホルダーとして{email}があることを確認してください。そうでなければClaudeは参照すべきカテゴリを知りません。"""

exercise_7_1_solution = """
USER TURN
Please classify emails into the following categories, and do not include explanations: 
<categories>
(A) Pre-sale question
(B) Broken or defective item
(C) Billing question
(D) Other (please explain)
</categories>

Here are a few examples of correct answer formatting:
<examples>
Q: How much does it cost to buy a Mixmaster4000?
A: The correct category is: A

Q: My Mixmaster won't turn on.
A: The correct category is: B

Q: Please remove me from your mailing list.
A: The correct category is: D
</examples>

Here is the email for you to categorize: {email}

ASSISTANT TURN
The correct category is:
"""
exercise_8_1_hint = """この演習の採点関数は、「I do not」、「I don't」、または「Unfortunately」というフレーズを含む回答を探しています。
Claudeが答えを知らない場合、何をすべきでしょうか？"""

exercise_8_2_hint = """この演習の採点関数は、「49-fold」というフレーズを含む回答を探しています。
関連する引用を抽出し、引用が十分な証拠を提供するかどうかを確認することで、Claudeに作業と思考プロセスを最初に示させてください。復習が必要な場合は第8章のレッスンを参照してください。"""

exercise_9_1_solution = """
You are a master tax acountant. Your task is to answer user questions using any provided reference documentation.

Here is the material you should use to answer the user's question:
<docs>
{TAX_CODE}
</docs>

Here is an example of how to respond:
<example>
<question>
What defines a "qualified" employee?
</question>
<answer>
<quotes>For purposes of this subsection—
(A)In general
The term "qualified employee" means any individual who—
(i)is not an excluded employee, and
(ii)agrees in the election made under this subsection to meet such requirements as are determined by the Secretary to be necessary to ensure that the withholding requirements of the corporation under chapter 24 with respect to the qualified stock are met.</quotes>

<answer>According to the provided documentation, a "qualified employee" is defined as an individual who:

1. Is not an "excluded employee" as defined in the documentation.
2. Agrees to meet the requirements determined by the Secretary to ensure the corporation's withholding requirements under Chapter 24 are met with respect to the qualified stock.</answer>
</example>

First, gather quotes in <quotes></quotes> tags that are relevant to answering the user's question. If there are no quotes, write "no relevant quotes found".

Then insert two paragraph breaks before answering the user question within <answer></answer> tags. Only answer the user's question if you are confident that the quotes in <quotes></quotes> tags support your answer. If not, tell the user that you unfortunately do not have enough information to answer the user's question.

Here is the user question: {QUESTION}
"""

exercise_9_2_solution = """
You are Codebot, a helpful AI assistant who finds issues with code and suggests possible improvements.

Act as a Socratic tutor who helps the user learn.

You will be given some code from a user. Please do the following:
1. Identify any issues in the code. Put each issue inside separate <issues> tags.
2. Invite the user to write a revised version of the code to fix the issue.

Here's an example:

<example>
<code>
def calculate_circle_area(radius):
    return (3.14 * radius) ** 2
</code>
<issues>
<issue>
3.14 is being squared when it's actually only the radius that should be squared>
</issue>
<response>
That's almost right, but there's an issue related to order of operations. It may help to write out the formula for a circle and then look closely at the parentheses in your code.
</response>
</example>

Here is the code you are to analyze:

<code>
{CODE}
</code>

Find the relevant issues and write the Socratic tutor-style response. Do not give the user too much help! Instead, just give them guidance so they can find the correct solution themselves.

Put each issue in <issue> tags and put your final response in <response> tags.
"""

exercise_10_2_1_solution = """system_prompt = system_prompt_tools_general_explanation + \"""Here are the functions available in JSONSchema format:

<tools>

<tool_description>
<tool_name>get_user</tool_name>
<description>
Retrieves a user from the database by their user ID.
</description>
<parameters>
<parameter>
<name>user_id</name>
<type>int</type>
<description>The ID of the user to retrieve.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>get_product</tool_name>
<description>
Retrieves a product from the database by its product ID.
</description>
<parameters>
<parameter>
<name>product_id</name>
<type>int</type>
<description>The ID of the product to retrieve.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_user</tool_name>
<description>
Adds a new user to the database.
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>The name of the user.</description>
</parameter>
<parameter>
<name>email</name>
<type>str</type>
<description>The email address of the user.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_product</tool_name>
<description>
Adds a new product to the database.
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>The name of the product.</description>
</parameter>
<parameter>
<name>price</name>
<type>float</type>
<description>The price of the product.</description>
</parameter>
</parameters>
</tool_description>

</tools>
"""