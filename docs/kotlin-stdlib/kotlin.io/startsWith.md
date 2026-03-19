

# startsWith

Determines whether this file belongs to the same root as other and starts with all components of other in the same order. So if other has N components, first N components of this must be the same as in other.

```kotlin
fun File.startsWith(other: File): Boolean(source)
```

```kotlin
import java.io.File

fun main() {
    val root = File("/home/user/projects")
    val fileInside = File("/home/user/projects/kotlin/Example.kt")
    val fileOutside = File("/home/user/other/Example.kt")

    println(fileInside.startsWith(root))   // true
    println(fileOutside.startsWith(root))  // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/starts-with.html)

    