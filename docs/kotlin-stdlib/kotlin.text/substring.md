

# substring

Returns a substring specified by the given range of indices.

```kotlin
fun String.substring(range: IntRange): String(source)
```

```kotlin
fun main() {
    val text = "Hello, Kotlin!"
    val sub = text.substring(7..11)
    println(sub) // prints "Kotlin"
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/substring.html)

    