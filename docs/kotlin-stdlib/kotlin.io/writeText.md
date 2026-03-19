

# writeText

Sets the content of this file as text encoded using UTF-8 or specified charset. If this file exists, it becomes overwritten.

```kotlin
fun File.writeText(text: String, charset: Charset = Charsets.UTF_8)(source)
```

```kotlin
import java.io.File
import java.nio.charset.Charset

fun main() {
    // Create a File instance pointing to "greeting.txt" in the current directory
    val file = File("greeting.txt")

    // Write a simple greeting to the file using UTF-8 encoding (default charset)
    file.writeText("Hello, Kotlin!", Charsets.UTF_8)

    // The file now contains the text "Hello, Kotlin!"
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/write-text.html)

    