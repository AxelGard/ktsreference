

# relativeToOrSelf

Calculates the relative path for this path from a base path.

```kotlin
fun Path.relativeToOrSelf(base: Path): Path(source)
```

```kotlin
import kotlin.io.path.Path
import kotlin.io.path.relativeToOrSelf

fun main() {
    val base   = Path("/home/user")
    val target = Path("/home/user/docs/file.txt")

    println(target.relativeToOrSelf(base))   // prints: docs/file.txt

    val unrelated = Path("/var/log/system.log")
    println(unrelated.relativeToOrSelf(base)) // prints: /var/log/system.log
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/relative-to-or-self.html)

    