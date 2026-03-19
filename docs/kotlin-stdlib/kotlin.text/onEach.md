

# onEach

Performs the given action on each character and returns the char sequence itself afterwards.

```kotlin
inline fun <S : CharSequence> S.onEach(action: (Char) -> Unit): S(source)
```

```kotlin
val text = "Kotlin"
val result = text.onEach { println("Char: $it") }
println("Returned string: $result")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/on-each.html)

    