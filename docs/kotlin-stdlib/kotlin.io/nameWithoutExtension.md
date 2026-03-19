

# nameWithoutExtension

Returns file's name without an extension.

```kotlin
val File.nameWithoutExtension: String(source)
```

```kotlin
import java.io.File

fun main() {
    val file = File("example.txt")
    println(file.nameWithoutExtension) // prints "example"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/name-without-extension.html)

    