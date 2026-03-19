

# inputStream

Constructs a new InputStream of this file and returns it as a result.

```kotlin
inline fun Path.inputStream(vararg options: OpenOption): InputStream(source)
```

```kotlin
import java.nio.file.Paths
import java.nio.file.StandardOpenOption

val path = Paths.get("example.txt")

path.inputStream().use { inputStream ->
    val text = inputStream.bufferedReader().readText()
    println(text)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/input-stream.html)

    