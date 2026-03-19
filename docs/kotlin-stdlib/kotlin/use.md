

# use

Executes the given block function on this resource and then closes it down correctly whether an exception is thrown or not.

```kotlin
@IgnorableReturnValueexpect inline fun <T : AutoCloseable?, R> T.use(block: (T) -> R): R(source)
```

```kotlin
import java.io.File

fun main() {
    // Read the first line from a text file using the `use` extension
    val firstLine = File("example.txt").bufferedReader().use { reader ->
        reader.readLine()
    }

    println("First line: $firstLine")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/use.html)

    