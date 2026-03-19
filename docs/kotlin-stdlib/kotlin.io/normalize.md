

# normalize

Removes all . and resolves all possible .. in this file name. For instance, File("/foo/./bar/gav/../baaz").normalize() is File("/foo/bar/baaz").

```kotlin
fun File.normalize(): File(source)
```

```kotlin
import java.io.File

fun main() {
    val original = File("/foo/./bar/gav/../baaz")
    val normalized = original.normalize()
    println("Original:   ${original.path}")
    println("Normalized: ${normalized.path}")
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/normalize.html)

    