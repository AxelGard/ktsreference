

# appendText

Appends text to the content of this file using UTF-8 or the specified charset.

```kotlin
fun File.appendText(text: String, charset: Charset = Charsets.UTF_8)(source)
```

```kotlin
import java.io.File
import java.nio.charset.Charset

fun main() {
    val file = File("example.txt")

    // Append a line using the default UTF-8 charset
    file.appendText("Hello, world!\n")

    // Append another line with a specified charset
    file.appendText("Goodbye, world!\n", Charset.forName("UTF-8"))
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/append-text.html)

    