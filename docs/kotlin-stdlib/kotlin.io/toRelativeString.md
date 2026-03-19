

# toRelativeString

Calculates the relative path for this file from base file. Note that the base file is treated as a directory. If this file matches the base file, then an empty string will be returned.

```kotlin
fun File.toRelativeString(base: File): String(source)
```

```kotlin
import java.io.File

fun main() {
    val base = File("src/main")
    val target = File("src/main/kotlin/com/example/MyClass.kt")

    // relative path from the base directory to the target file
    val relativePath = target.toRelativeString(base)
    println(relativePath) // prints: "kotlin/com/example/MyClass.kt"

    // when the target is the same as the base, an empty string is returned
    val sameFile = File("src/main")
    println(sameFile.toRelativeString(base)) // prints: ""
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/to-relative-string.html)

    