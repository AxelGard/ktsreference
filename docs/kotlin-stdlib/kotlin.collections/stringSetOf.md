

# stringSetOf

Creates a new instance of the specialized implementation of HashSet with the specified String elements, which elements the keys as properties of JS object without hashing them.

```kotlin
fun stringSetOf(vararg elements: String): HashSet<String>(source)
```

```kotlin
fun main() {
    val colors = stringSetOf("red", "green", "blue")
    colors.add("yellow")
    println(colors)                     // [red, green, blue, yellow]
    println(colors.contains("green"))   // true
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/string-set-of.html)

    