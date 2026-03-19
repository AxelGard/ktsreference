

# minusPolymorphicKey

Returns empty coroutine context if the element is associated with the given key in a polymorphic manner or null otherwise. This method returns empty context if either Element.key is equal to the given key or if the key is associated with Element.key via AbstractCoroutineContextKey. See AbstractCoroutineContextKey for the example of usage.

```kotlin
@ExperimentalStdlibApifun CoroutineContext.Element.minusPolymorphicKey(key: CoroutineContext.Key<*>): CoroutineContext(source)
```

```kotlin
import kotlinx.coroutines.*
import kotlin.coroutines.*

object MyKey : CoroutineContext.Key<MyElement>
class MyElement(val id: Int) : CoroutineContext.Element {
    override val key: CoroutineContext.Key<*> = MyKey
}

@OptIn(ExperimentalStdlibApi::class)
fun main() {
    val element = MyElement(42)
    val context = element + Dispatchers.Default

    println("Initial context: $context")            // contains MyElement and Default dispatcher

    // Remove the element by its key
    val empty = element.minusPolymorphicKey(MyKey)
    println("After minusPolymorphicKey(MyKey): $empty") // EmptyCoroutineContext
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines/minus-polymorphic-key.html)

    