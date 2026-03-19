

# isRooted

Determines whether this file has a root or it represents a relative path.

```kotlin
val File.isRooted: Boolean(source)
```

```kotlin
import java.io.File

fun main() {
    val absolutePath = File("/usr/local/bin")
    val relativePath = File("src/main/kotlin")

    println("${absolutePath.path} is rooted? ${absolutePath.isRooted}")   // true
    println("${relativePath.path} is rooted? ${relativePath.isRooted}")   // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/is-rooted.html)

    