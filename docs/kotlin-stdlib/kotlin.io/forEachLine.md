

# forEachLine

Reads this file line by line using the specified charset and calls action for each line. Default charset is UTF-8.

```kotlin
fun File.forEachLine(charset: Charset = Charsets.UTF_8, action: (line: String) -> Unit)(source)
```

```kotlin
import java.io.File

fun main() {
    val file = File("example.txt")
    file.forEachLine { line ->
        println(line)
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/for-each-line.html)

    