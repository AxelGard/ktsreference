

# isHidden

Checks if the file located by this path is considered hidden.

```kotlin
inline fun Path.isHidden(): Boolean(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.isHidden

fun main() {
    val visibleFile = Paths.get("example.txt")
    val hiddenFile  = Paths.get(".hiddenExample")

    println("Is ${visibleFile.fileName} hidden? ${visibleFile.isHidden()}")
    println("Is ${hiddenFile.fileName} hidden? ${hiddenFile.isHidden()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/is-hidden.html)

    