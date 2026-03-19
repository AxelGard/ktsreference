

# relativeToOrNull

Calculates the relative path for this path from a base path.

```kotlin
fun Path.relativeToOrNull(base: Path): Path?(source)
```

```kotlin
import kotlin.io.path.Path
import kotlin.io.path.relativeToOrNull

fun main() {
    val base = Path("/home/user")
    val file = Path("/home/user/docs/report.pdf")

    val relative = file.relativeToOrNull(base)
    println(relative)          // prints: docs/report.pdf

    val unrelated = Path("/var/log")
    println(unrelated.relativeToOrNull(base)) // prints: null
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/relative-to-or-null.html)

    