

# invariantSeparatorsPath

Returns path of this File using the invariant separator '/' to separate the names in the name sequence.

```kotlin
val File.invariantSeparatorsPath: String(source)
```

```kotlin
import java.io.File

fun main() {
    val file = File("src", "main", "kotlin")
    println(file.invariantSeparatorsPath)   // prints: src/main/kotlin
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/invariant-separators-path.html)

    