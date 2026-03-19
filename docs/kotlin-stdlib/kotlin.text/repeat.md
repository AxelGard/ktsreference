

# repeat

Returns a string containing this char sequence repeated n times.

```kotlin
expect fun CharSequence.repeat(n: Int): String(source)
```

```kotlin
fun main() {
    val pattern = "ab"
    val repeated = pattern.repeat(3)   // "ababab"
    println(repeated)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/repeat.html)

    