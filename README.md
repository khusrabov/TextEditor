<h1 id="text-editor">Text Editor</h1>
<blockquote>
<p>Консольный текстовый редактор - самостоятельная компьютерная программа, предназначенная для создания и изменения текстовых данных в общем и текстовых файлов, в частности.

Консольный текстовой редактор предназначен для работы с текстовыми файлами в интерактивном режиме. Он позволяет просматривать содержимое текстовых файлов и производить над ними различные действия: вставку, удаление и копирование текста.</p>
</blockquote>

<h1 id="-arncpp">Базовый Функционал:</h1>

* Возможность редактирования файла
* Перемещение по тексту при помощи “стрелок” - по словам, в начало/конец строки. 
* Удаление строк и слов
* Текстовый поиск и замена
* Хоткеи для сохранения и выхода
    
<h2 id="-pycharm">Как запустить текстовый редактор через консоль</h2>
<details>
<summary><strong>Первый этап: установка python.
<h5 id="-python3"><em>Если у вас уже установлен python3 - пропустите этот этап</em></h5></strong></summary>
<p><strong>1. Скачайте python3 с официального <a href="https://www.python.org/downloads/">сайта</a> и установите его.</strong>
<strong>2. Во время установки <em>обязательно</em> поставьте галочку &quot;Add Python 3.x to PATH&quot;.</strong>
<img src="https://python-scripts.com/wp-content/uploads/2018/06/win-install-dialog.40e3ded144b0.png" alt="add path screenshot"></p>
<p><strong>3. Когда установка закончится запустите консоль.</strong>
</details>
<strong>Второй этап: скачивание и запуска проекта.</strong>
<p><strong>1. Скачайте проект с github любым удобным для вас способом.</strong></p>
<p><strong>2. В консоли перейдите в папку. </strong>
<p><strong>3. Запустите текстовый редактор.</strong>
<p><strong>4. Наслаждайтесь!</strong>
<details>
<summary>Команды, которые нужно выполнить, для запуска через консоль:</summary>
<p><code>git clone git@github.com:khusrabov/TextEditor.git</code></p>
<p><code>cd</code></p>
<p><code>python TextEditor.py</code></p></details>

<h2 id="-pycharm">Как запустить текстовый редактор на PyCharm</h2>
<p><strong>1. Создайте пустой проект на PyCharm: (<em>File -&gt; New Project</em>)</strong></p>
<p><strong>2. Зайдите в убунту-консоль, перейдите в папку с проектом (с помощью cd)</strong></p>
<p><strong>3. Скачайте проект с github любым удобным для вас способом. </strong></p>
<p><strong>4. Подождите, пока скачается. После скачивания откройте проект в PyCharm.</strong></p>
<p><strong>5. Запустите файл TextEditor.py</strong></p>
<p><strong>6. Запустив текстовый редактор введите свои первые слова!</strong></p>

<h1 id="-">Скрины использования функционала и примеры работы биндов:</h1>

* Интерфейс:
    <p> Вас встречает текстовый редактор с черным фоном и зеленным цветом шрифта, три меню: File, View, Edit, 
    о которых более подробно будет написано чуть позже, а также две кнопки Find & Replace,
    с рамкой ввода для каждой кнопки текста.
<p><img src="screenshots/interface.png" alt="Menu" title="Интерфейс">

* Работа с кнопками Find & Replace:
 <p> Давайте найдем все повторения "the" в 7 сонате Шекспира.
<p><img src="screenshots/find.png" alt="Find" title="FIND">
<p> Теперь поменяем на "replaced_the".
<p><img src="screenshots/Replaced.png" alt="Replace" title="Replace">

* File, View, Edit:
<p><img src="screenshots/File.png" alt="File" title="FILE"></p>
<p><img src="screenshots/View.png" alt="View" title="VIEW"></p>
<p><img src="screenshots/Edit.png" alt="Edit" title="Edit"></p>

В приложение также забинжены множество команд. 
Сочетания клавиш указаны справа от всех действий. Но вот полный список:
* File Menu:
  
  * Control-n = new_file
  * Control-o = open_file
  * Control-s = save_file
  * Control-Shift-s = save_file_as
  * Control-q = close_file

* Edit Menu:
  * Control-x = cut
  * Control-c = copy
  * Control-v = paste
  * Control-d = delete
  * Control-a = select all

* Text bind:

  * Left (<-)  
  * Right (->)
  * Up (/\)
  * Down (\/)
  * Control-Shift-Left = move_to_start
  * Control-Shift-Right = move_to_end
  * Control-w = move_to_start_of_line
  * Control-e = move_to_end_of_line
  * Control-Right = move_cursor_forward
  * Control-Left = move_cursor_backward
