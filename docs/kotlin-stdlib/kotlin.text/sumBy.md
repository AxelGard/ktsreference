

# sumBy

Warning since 1.5

```kotlin
inline fun CharSequence.sumBy(selector: (Char) -> Int): Int(source)
```

val text = "abc"
val sum = text.sumBy { it - 'a' + 1 }
println(sum)

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/sum-by.html)

    