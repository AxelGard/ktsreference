

# extension

Returns the extension of this file (not including the dot), or an empty string if it doesn't have one.

```kotlin
val File.extension: String(source)
```

```kotlin
import java.io.File

fun main() {
    val fileWithExt = File("sample.pdf")
    println("Extension of ${fileWithExt.name}: ${fileWithExt.extension}") // prints: pdf

    val fileWithoutExt = File("LICENSE")
    println("Extension of ${fileWithoutExt.name}: ${fileWithoutExt.extension}") // prints: (empty string)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/extension.html)

    