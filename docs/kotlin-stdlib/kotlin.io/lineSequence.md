

# lineSequence

Returns a sequence of corresponding file lines.

```kotlin
fun BufferedReader.lineSequence(): Sequence<String>(source)
```

```kotlin
import java.io.File

fun main() {
    // Read all lines from a file and print them
    File("example.txt").bufferedReader().lineSequence()
        .forEach { line -> println(line) }

    // Count non-empty lines in the same file
    val nonEmptyLines = File("example.txt")
        .bufferedReader()
        .lineSequence()
        .count { it.isNotBlank() }

    println("Non‑empty lines: $nonEmptyLines")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/line-sequence.html)

    