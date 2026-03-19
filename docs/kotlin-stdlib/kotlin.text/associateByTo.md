

# associateByTo

Populates and returns the destination mutable map with key-value pairs, where key is provided by the keySelector function applied to each character of the given char sequence and value is the character itself.

```kotlin
@IgnorableReturnValueinline fun <K, M : MutableMap<in K, in Char>> CharSequence.associateByTo(destination: M, keySelector: (Char) -> K): M(source)
```

```kotlin
fun main() {
    val destination = mutableMapOf<Char, Char>()
    val text = "kotlin"

    val result = text.associateByTo(destination) { it }

    println(result)   // {k=k, o=o, t=t, l=l, i=i, n=n}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/associate-by-to.html)

    