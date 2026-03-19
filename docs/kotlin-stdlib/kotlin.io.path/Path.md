

# Path

Converts the provided path string to a Path object of the default filesystem.

```kotlin
inline fun Path(path: String): Path(source)
```

```kotlin
import kotlin.io.path.*

fun main() {
    val path = Path("sample.txt")

    if (!path.exists()) {
        path.writeText("Hello Kotlin Path!")
    }

    println("File content: ${path.readText()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/-path.html)

    