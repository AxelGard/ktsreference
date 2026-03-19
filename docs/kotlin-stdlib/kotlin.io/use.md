

# use

Executes the given block function on this resource and then closes it down correctly whether an exception is thrown or not.

```kotlin
@IgnorableReturnValueinline fun <T : Closeable?, R> T.use(block: (T) -> R): R(source)
```

```kotlin
import java.io.BufferedReader
import java.io.FileReader

fun readFirstLine(path: String): String? =
    BufferedReader(FileReader(path)).use { reader ->
        reader.readLine()   // automatically closes the reader afterwards
    }
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/use.html)

    